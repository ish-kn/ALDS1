#include<bits/stdc++.h>
using namespace std;

struct foo {
    int id, name;
};

int main() {
    foo f, g;

    f.id = 0;
    f.name = 1;
    g = f;

    cout << g.id << g.name << endl;
    g.id = 3; g.name = 4;
    cout << f.id << f.name << endl;
    cout << g.id << g.name << endl;
    return 0;
}

