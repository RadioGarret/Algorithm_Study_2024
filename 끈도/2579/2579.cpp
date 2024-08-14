//////////////////////////////////////////////////////
// 2024.08.14 / 백준 2579 / 계단 오르기 (실버 3) / DP
// https://www.acmicpc.net/problem/2579
//////////////////////////////////////////////////////

#include <iostream>
#include <algorithm>
using namespace std;

int N;
int score[301];
int DP[301];

int dp(int level){
    if (level == 0) return 0;
    if (level == 1) return score[1];
    if (level == 2) return score[1] + score[2];
    if (DP[level] > 0) return DP[level];
    return DP[level] = max(dp(level - 3) + score[level - 1] + score[level], dp(level-2) + score[level]);
}


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int i = 1; i<=N; i++){
        cin >> score[i];
    }

    cout << dp(N);
    return 0;

}
