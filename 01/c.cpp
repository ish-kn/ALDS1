#include<bits/stdc++.h>
using namespace std;

static const int MAX = 1e7;

bool isprime[MAX + 1];

void eratos() {
    memset(isprime, true, sizeof(isprime));
    isprime[0] = isprime[1] = false;

    for (int i = 2; i * i <= MAX; i++) {
        if (isprime[i]) {
            int j = i + i;
            while (j <= MAX) {
                isprime[j] = false;
                j += i;
            }
        }
    }
}

int main() {
    eratos();
    
    int cnt = 0;
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        int x; scanf("%d", &x);
        cnt += (isprime[x]) ? 1 : 0;
    }
    
    cout << cnt << endl;
    
    return 0;
}
