// #include <iostream>

// int main()
// {
//     std::cout << "Hello World!" << std::endl;

//     return 0;
// }

// #include <stdio.h>
// #include <iostream>


// int main(){
//   int a = 45;
//   printf("char : %d\n", sizeof(char));
//   printf("short int : %d\n", sizeof(short int));
//   printf("int : %d\n", sizeof(int));
//   printf("long int : %d\n", sizeof(long int));
//   printf("float : %d\n", sizeof(float));
//   printf("double : %d\n", sizeof(double));
//   printf("long double : %d\n", sizeof(long double));
//   std::cout << a << std::endl;

//   return 0;
// }

// #include <iostream>
// using namespace std;
// int main() {
//     int a = 0b1010;// 実際上は 0b101101、あるいは 0x2d と書く
//     // a = a << 2;
//     int b = 25;
//     std::cout << a << std::endl;
// }


#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n = 3;

    // {0, 1, ..., n-1} の部分集合の全探索
    for (int bit = 0; bit < (1<<n); ++bit) {
        // 初期化
        vector<int> S;
        for (int i = 0; i < n; ++i) {
            // cout << i;
            // cout << (bit & (1<<i)) << endl;
            if (bit & (1<<i)) { // 列挙に i が含まれるか
                // cout << bit << (1<<i) << (bit & (1<<i)) << endl;
                cout << i << endl;
                S.push_back(i);
            }
        }

        // cout << bit << ": {";
        for (int i = 0; i < (int)S.size(); ++i) {
            // cout << S[i] << " ";
        }
        // cout << "}" << endl;
    }
}

