# 백준 문제(2021.5.25)
# 13136번) ACM-ICPC 대회의 대회장은 R행 C열의 직사각형 형태로 좌석이 배치되어 있다. 
# 대회가 시작하기 전에는 참가자들이 아무것도 만지면 안 되기 때문에 진행자는 
# 'Do not touch ANYTHING!!!'을 연신 외친다.
# 하지만, 진행자가 성대결절에 걸리면서 'Do not touch ANYTHING!!!'을 외칠 수 없는 처지가 되었다. 
# 따라서 주최측은 CCTV를 설치하여 참가자들을 감시하려고 한다. 
# 이때, 각 CCTV는 N행 N열의 직사각형 영역의 좌석을 촬영할 수 있다.
# 모든 좌석을 전부 촬영하도록 CCTV를 배치할 때,n 최소 몇 개의 CCTV가 필요할까?
# INPUT) 첫 번째 줄에 좌석의 세로 크기, 가로 크기 R, C와 한 대의 CCTV가 수용할 수 있는 
# 범위 N이 주어진다. (1 ≤ R, C, N ≤ 1,000,000)
import math

r, c, n = map(int, input().split())

print(math.ceil(r/n) * math.ceil(c/n))