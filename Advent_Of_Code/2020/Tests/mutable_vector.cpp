#include <iostream>
#include <vector>

using namespace std;

void changeVector1(vector<int> &test){
    test[1] = 10;
}
void changeVector2(vector<int> &test){
    test.insert(test.begin(),20);
}

void printVector(vector<int> test){
    for(int i : test){
        cout << i << " ";
    }
    cout << endl;
}

int  main(){
    vector<int> test;

    test.push_back(1);
    test.push_back(2);
    test.push_back(3);
    test.push_back(4);

    changeVector1(test);
    // changeVector2(test);

    printVector(test);

}