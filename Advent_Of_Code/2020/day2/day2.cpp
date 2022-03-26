#include <iostream>
#include <list>
#include <fstream>
#include <string>

using namespace std;

struct range{
    int min;
    int max;
};
struct passwordCheck{
    range passRange;
    char character;
    string password;
};

void openAndReadFile(list<string> &, string);
void readFile(ifstream &, list<string> &);
void printList(list<string>);

int doPart1(list<string>);
int doPart2(list<string>);
passwordCheck parseLine(string);
int validatePassword(passwordCheck);
int getOccurenceofChar(string, char);
int newValidatePassword(passwordCheck);

int main(){
    list<string> items;
    openAndReadFile(items, "input");
    //printList(items);

    //int sum = doPart1(items);
    //cout << "Sum: " << sum << "\n";

    int sum = doPart2(items);
    cout << "Sum: " << sum << "\n";

    return 0;
}

void openAndReadFile(list<string> &items, string input){
    ifstream myFileStream;
    myFileStream.open(input);

    if( myFileStream.is_open() ){
        readFile(myFileStream, items);
    }
    myFileStream.close();
}

void readFile(ifstream &myFileStream, list<string> &items){
    for( string myString; getline(myFileStream, myString);){
        items.push_back(myString);
    }
}

int doPart1(list<string> items){
    int sum = 0;
    for(string lineItem : items){
        passwordCheck passwordToken = parseLine(lineItem);

        sum += validatePassword(passwordToken);
    }
    return sum;
}

int doPart2(list<string> items){
    int sum = 0;
    for(string lineItem : items){
        passwordCheck passwordToken = parseLine(lineItem);

        sum += newValidatePassword(passwordToken);
    }
    return sum;
}

/* 
//  * password line is min-max char: password
 *  seperate into 3 portions, range char password
 *  1: split range by delim "-"
 *  2: remove trailing ":" from char
 *  3: just grab password
 */
passwordCheck parseLine(string lineItem){
    passwordCheck passwordToken;

    string delim = " ";
    int start = 0;

    // FIRST PORTION
    int first_portion = lineItem.find(delim, start); 
    string min_max = lineItem.substr(start, first_portion); // min-max:
    int hyphen_location = min_max.find("-"); //eg. 3
    string min_range = min_max.substr( start, hyphen_location );
    string max_range = min_max.substr( hyphen_location+1, min_max.find(":") - hyphen_location );

    // cout << "Min Range: " << min_range+1 << "$ ";
    // cout << " Max Range: " << max_range+1 << "$ \n";

    range _range;
    _range.min = stoi(min_range);
    _range.max = stoi(max_range);

    // cout << "First Index: " << _range.min+1 << "\n";
    // cout << "Second Index: " << _range.max+1 << "\n";

    //SECOND PORTION
    char character = lineItem[first_portion+1];

    // cout << "Character: " << character << "\n"; 

    //THIRD PORTION
    int second_portion = lineItem.find(delim, first_portion+1);
    string password = lineItem.substr(second_portion+1, lineItem.length() - second_portion);
    
    // cout << "Password: $" << password << "$\n";

    passwordToken.passRange = _range;
    passwordToken.character = character;
    passwordToken.password = password;

    return passwordToken;
}

int validatePassword(passwordCheck passwordToken){
    int count = getOccurenceofChar(passwordToken.password, passwordToken.character);
    //cout << "Occurence: " << count << "\n";

    if(passwordToken.passRange.min <= count && count <= passwordToken.passRange.max)
        return 1;
    return 0;
}

int getOccurenceofChar(string str, char c){
    int sum = 0;
    char *end = &str.back();
    for (char *start = &str[0]; start <= end; start++)
        if (*start == c)
            sum ++;
    return sum;
}

int newValidatePassword(passwordCheck passwordToken){
    string password = passwordToken.password;
    int a = passwordToken.passRange.min;
    int b = passwordToken.passRange.max;
    char c = passwordToken.character;

    // cout << "Char: " << c << " First: " << password[a-1] << " Second: " << password[b-1] << "\n";
    if(!(password[a-1] == c) != !(password[b-1] == c)){
        // cout << "Valid\n"; 
        return 1;
    }
    // cout << "Invalid\n"; 
    return 0;
}

void printList(list<string> items){
    cout << "items { ";
    for(string item : items){
        cout << item << ", ";
    }
    cout << "}; \n";
}

