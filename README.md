# coding_test
coding_test algorithm 

## 3. greedy 알고리즘
   1. 최소한 동전개수로 거스름돈 주기: 큰단위부터 돈을 거슬러줘야함, 시간복잡도는 동전의 총 종류에 영향을 받음, //와 %연산자를 사용해 for문 더 간단하게 구상할 필요 있음 
   2. 큰 수의 법칙 : 최대 k번 더하고 두번쨰로 큰수를 더하는 것을 반복하면 되므로 반복되는 배열을 묶어 하나의 배열처럼 묶음으로 처리하는 코드를 연습해봄 
   3. 숫자 카드 게임
   4. 1이 될때까지 두과정 반복해서 수행하기 : 최대한 나누는 과정을 많이 넣으면 된다 !while 조건문으로 n이 k이상인 경우를 확인해주기 !!!!! 만약 나눈 후에도 1보다 크면 1 빼주는 경우도 생각하기 -> 제일 중요한 나누는 걸 먼저 많이 해준다는 생각으로 알고리즘 수정하기. 

## 4. 구현
   0.완전 탐색: 모든 경우의 수를 주저 없이 다 계산 하는 해결방법 / 시뮬레이션: 문제에서 제시한 알고리즘을 한단계씩 차례대로 직접 수행하는 방법
   1. 상하좌우 문제: 반복되는 코드를 move_types라는 변수를 선언해 for문으로 돌리는 방법 공부, 새로운 변수 선언하고 후에 if문을 넣어 무시하게 되는 경우는 기존변수에 새로운 변수를 대입하지 않고 continue처리해서 무시하기
   2. 시각: 3중 반복문으로 처리, 시각안에 특정 숫자 있는지 확인하려면 if '특정숫자' in str()+str() 
   3. 왕실의 나이트: ord() 특정한 한 문자를 아스키 코드값으로 변환하는 것 
   4. 게임 개발 : 일주일 후에 다시 도전.. 
