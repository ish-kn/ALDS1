#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;
#define MAX 2000000
#define INF (1<<30)

int H , A[MAX+1];

void maxHeapify(int i) {
    int l, r, largest;
    l = 2 * i;
    r = 2 * i + 1;

    if (l <= H && A[l] > A[i]) largest = l;
    else largest = i;
    if (r <= H && A[r] > A[largest]) largest = r;

    if (largest != i) {
        swap(A[i], A[largest]);
        maxHeapify(largest);
    }
}

int extract() {
    int maxv;
    if (H < 1) return -INF;
    maxv = A[1];
    A[1] = A[H--];
    maxHeapify(1);
    return maxv;
}

void increaseKey(int i, int key) {
    if (key < A[i]) return;
    A[i] = key;
    while (i > 1 && A[i / 2] < A[i]) {
        swap(A[i], A[i / 2]);
        i = i / 2;
    }
}

void insert(int key) {
    H++;
    A[H] = -INF;
    increaseKey(H, key);
}

int main() {
    int k;
    char com[10];

    while (1) {
        scanf("%s", com);
        if (com[0] == 'e' && com[1] == 'n') break;
        if (com[0] == 'i') {
            scanf("%d", &k);
            insert(k);
        } else {
            printf("%d\n", extract());
        }
    }
    
    return 0;
}
