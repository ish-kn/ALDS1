#include<cstdio>
#include<queue>
using namespace std;

int main() {
    char com[20];
    priority_queue<int> PQ;

    while (1) {
        scanf("%s", com);
        if (com[0] == 'i') {
            int k; scanf("%d", &k);
            PQ.push(k);
        } else if (com[1] == 'x') {
            printf("%d\n", PQ.top());
            PQ.pop();
        } else break;
    }

    return 0;
}
