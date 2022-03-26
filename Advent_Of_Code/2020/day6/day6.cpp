#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include "utilities.cpp"

using namespace std;

void doPart1(vector<string>);
int countUniqueOccurence(string);

void doPart2(vector<string>);
vector<char> getUniqueOccurence(string);
int countCommonOccurence(vector<vector<char> >);

int main(){
    vector<string> contents = openAndReadFile("input");

    vector<string> groups = makeLineGroups(contents);

    doPart2(groups);

}

void doPart1(vector<string> groups){
    int sum = 0;
    for(string group : groups){
        int count = countUniqueOccurence(group);
        sum += count;
        // cout << "count: " << count << endl;
    }
    cout << "Sum: " << sum << endl;
}

int countUniqueOccurence(string group){
    vector<char> seen;
    int sum = 0;
    for(char c : group){
        if (isalpha(c) && find(seen.begin(), seen.end(), c) == seen.end()){
            seen.push_back(c);
            sum++;
        }
    }
    return sum;
}

void doPart2(vector<string> groups){
    int sum = 0;
    // printVector(groups);
    for(string group : groups){
        vector<string> responses = getAllWords(group);
        vector<vector<char> > seenList;
        for(string response : responses){
            seenList.push_back( getUniqueOccurence(response) );
        }
        sum += countCommonOccurence(seenList);
    }
    cout << "sum: " << sum << endl;
}

vector<char> getUniqueOccurence(string response){
    vector<char> seen;
    for(char c : response){
        if (isalpha(c) && find(seen.begin(), seen.end(), c) == seen.end()){
            seen.push_back(c);
        }
    }
    return seen;
}

int countCommonOccurence(vector<vector<char> > seenList){
    int sum = 0;
    vector<char> baseList = seenList[0];
    for(char c : baseList){
        for(int i = 1; i < seenList.size(); i++){
            vector<char> currentList = seenList[i];
            if(find(currentList.begin(),currentList.end(),c) == currentList.end())
                goto NOTFOUND;
        }

        sum++;

        NOTFOUND:;
    }
    return sum;
}