#include <iostream>
#include <string>
#include <vector>

using namespace std;

void doPart1(vector<string>);

void parseBagLine(string);
void updateKnownBags(vector<bag>&, bag);

//recursive
bool isInBagContains(bag);

struct bag{
    string name;
    vector<bag> contains;
};


int main(){



    return 0;
}


void doPart1(vector<string> contents){
    vector<bag> knownBags;

    for(string line : contents){
        parseBagLine(line);
    }
}

void parseBagLine(string line){

}

void updateKnownBags(vector<bag> &knownBags, bag newBag){

}

bag isInBagContains(bag currentBag, string name){
    if(currentBag.contains.empty()){
        return (bag) NULL;
    }
    if(find(currentBag.contains.begin(), currentBag.contains.end(), name) != currentBag.contains.end()){
        return currentBag;
    }

    for(bag bags : currentBag.contains){
        bag temp = isInBagContains(bags,name);
        if(temp != (bag)NULL){
            return temp;
        }
    }
}