```bash
pip install scipy==1.11.1
pip install numpy==1.25.1
pip install matplotlib==3.7.2
pip install gym==0.26.2
pip install pyglet==2.0.8
```

교수님이 주신 코드 최초로 board & env 수정 버전
info에 invaild_moves 적용 안한 버전
qrdqn 적용 안한 버전

현재 adj_locs가 상하좌우 4개만 보고 있음 사목 특성상 대각선도 고려를 해야하는데 이것도 설정해야할듯
돌려보니까 adj_locs가 적용이 안되서 필요에 따라서 삭제하거나 하면 될듯

