#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

static const int N = 1000;

int lcs(string X, string Y) {
    int c[N + 1][N + 1];
    int m = X.size();
    int n = Y.size();
    memset(c, 0, sizeof(c));

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (X[i - 1] == Y[j - 1]) 
                c[i][j] = c[i - 1][j - 1] + 1;
            else
                c[i][j] = max(c[i - 1][j], c[i][j - 1]);
        }
    }

    return c[m][n];
}

int main() {
    string s1, s2;
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s1 >> s2;
        cout << lcs(s1, s2) << endl;
    }
    return 0;
}
