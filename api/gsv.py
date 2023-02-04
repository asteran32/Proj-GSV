import requests
import cv2
import numpy as np

class GSV():
    def __init__(self, api_key:str) -> None:
        self.height = 400
        self.width = 600
        self.api_key = api_key
    
    def get_url(self, lat: float, lon: float, heading: float, pitch: float):
        """_summary_
        Args:
            lat (float): 위도
            lon (float): 경도
            fov (float, optional): 이미지 수평시야 (90 ~ 120). Defaults to 90.
            heading (float, optional): 카메라 나침반 방향(0 ~ 360). Defaults to 0.
            pitch (float, optional): 스트리트 뷰 차량을 기준으로 카메라의 위 또는 아래 각도(-90 ~ 90). Defaults to 0.

        Returns:
            _type_: request url
        """
        search_url = f'https://maps.googleapis.com/maps/api/streetview?size={self.width}x{self.height}&location={lat},{lon}&heading={heading}&pitch={pitch}&key={self.api_key}&source=outdoor&return_error_code=true'
        return search_url

    def get_gsv_veiw_image(self, lat: float, lon: float, heading:float = 0, pitch:float = 0):
        """gsv request test"""
        url = self.get_url(lat, lon, heading, pitch)
        # print(url) # for test
        res = requests.request('GET', url)
        if res.status_code == 404:
            return None
        image = cv2.imdecode(np.frombuffer(res.content, dtype=np.uint8), cv2.IMREAD_COLOR)
        return image
    