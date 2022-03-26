#include <iostream>
#include <list>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

list<string> openAndReadFile(string);
void readFile(ifstream &, list<string> &);

vector<vector<char> > loadMap(list<string>);
void printMap(vector<vector<char> >);

void doPart1(vector<vector<char> > &);
void doPart2(vector<vector<char> > &);
int traverseMapWithSteps(int, int, vector<vector<char> > &);

int main(){

    list<string> items = openAndReadFile("input");

    vector<vector<char> > snowMap = loadMap(items);

    //doPart1(snowMap);

    doPart2(snowMap);

    //printMap(snowMap);

    return 0;
}

list<string> openAndReadFile(string input){
    ifstream myFileStream;
    list<string> items;
    myFileStream.open(input);

    if( myFileStream.is_open() ){
        readFile(myFileStream, items);
    }else{
        cout << "File " << input << " couldn't open." << endl;
        exit(2);
    }
    myFileStream.close();
    return items;
}

void readFile(ifstream &myFileStream, list<string> &items){
    for( string myString ; getline(myFileStream, myString) ; ){
        items.push_back(myString);
    }
}

vector<vector<char> > loadMap(list<string> items){
    vector<vector<char> >  snowMap;
    for(string line : items){
        vector<char> mapline;
        for( char c : line){
            mapline.push_back(c);
        }
        snowMap.push_back(mapline);
    }
    return snowMap;
}

void printMap(vector<vector<char> > snowMap){
    for(vector<char> line : snowMap){
        for(char c : line){
            cout << c;
        }
        cout << endl;
    }
}

void doPart1(vector<vector<char> > &snowMap){
    int height = snowMap.size();
    int width = snowMap[0].size();

    int x = 0;
    int y = 0;
    int step = 3;


    int sum = 0;
    while (y < height){
        if (snowMap[y][x] == '#'){
            //snowMap[y][x] = 'X';
            sum++;
        }
        // else 
        //     snowMap[y][x] = 'O';
        x = (x + step) % width;
        y += 1;
    }
    cout << "sum: " << sum << endl;
}

void doPart2(vector<vector<char> > &snowMap){
    long a = traverseMapWithSteps(1,1, snowMap);
    long b = traverseMapWithSteps(3,1, snowMap);
    long c = traverseMapWithSteps(5,1, snowMap);
    long d = traverseMapWithSteps(7,1, snowMap);
    long e = traverseMapWithSteps(1,2, snowMap);

    long sum = a * b * c * d * e;

    cout << "Part 2 Sum = a * b * c * d * e = " << sum << endl;

}

int traverseMapWithSteps(int right, int down, vector<vector<char> > &snowMap){
    int height = snowMap.size();
    int width = snowMap[0].size();

    int x = 0;
    int y = 0;

    int sum = 0;
    while (y < height){
        if (snowMap[y][x] == '#')
            sum++;
        x = (x + right) % width;
        y += down;
    }
    cout << "sum: " << sum << endl;
    return sum;
}