#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "utilities.cpp"

using namespace std;

// vector<string> openAndReadFile(string);
// void readFile(ifstream &, vector<string> &);

void doPart1(vector<string>);

vector<string> getPassports(vector<string>);
int checkPassport(string);

void doPart2(vector<string>);
int validatePassport(string);
int validateKey(string, string);

void printList(vector<string>);

int  validateHgt(string); 
int  validateHcl(string);
int  validateEcl(string);
int  validatePid(string);

int main(){
    vector<string> contents = openAndReadFile("input");

    doPart2(contents);
}

// vector<string> openAndReadFile(string input){
//     ifstream myFileStream;
//     vector<string> items;
//     myFileStream.open(input);

//     if( myFileStream.is_open() ){
//         readFile(myFileStream, items);
//     }else{
//         cout << "File " << input << " couldn't open." << endl;
//         exit(2);
//     }
//     myFileStream.close();
//     return items;
// }

// void readFile(ifstream &myFileStream, vector<string> &items){
//     for( string myString ; getline(myFileStream, myString) ; ){
//         items.push_back(myString);
//     }
// }

void doPart1(vector<string> contents){

    vector<string> passports = getPassports(contents);

    //printList(passports);

    int sum = 0;
    for(string passport : passports)
        sum += checkPassport(passport);

    cout << "sum: " << sum << endl;

}

vector<string> getPassports(vector<string> contents){
    vector<string> passports;
    passports.push_back("");
    for(vector<string>::iterator line = contents.begin(); line != contents.end(); ++line){
        if(*line==""){
            passports.push_back("");
            continue;
        }else{
            passports.back() += *line + " ";
        }
    }
    return passports;
}

int checkPassport(string passport){
    if(passport.find("byr") != -1 && passport.find("iyr") != -1 && passport.find("eyr") != -1
        && passport.find("hgt") != -1 && passport.find("hcl") != -1 && passport.find("ecl") != -1
        && passport.find("pid") != -1)
        return 1;
    return 0;
}


void doPart2(vector<string> contents){

    vector<string> passports = getPassports(contents);

    //printList(passports);

    int sum = 0;
    for(string passport : passports)
        sum += validatePassport(passport);

    cout << "sum: " << sum << endl;

}

int validatePassport(string passport){
    vector<string> words = getAllWords(passport);
    cout << "Validating New Passport" << endl;
    //printList(words);
    for(string word : words){
        string key = word.substr(0,3);
        string value = word.substr(word.find(':')+1);

        if (!validateKey(key,value)){
            cout << "[INVALID] " << "Key: " << key << " Value: " << value << endl;
            return 0;
        }
         cout << "[VALID] " << "Key: " << key << " Value: " << value << endl;
    }
    return 1;
}

int validateKey(string key, string value){
    if(key == "byr"){
        return 1920 <= stoi(value) && stoi(value) <= 2002;
    } else if(key == "iyr"){
        return 2010 <= stoi(value) && stoi(value) <= 2020;
    } else if(key == "eyr"){
        return 2020 <= stoi(value) && stoi(value) <= 2030;
    } else if(key == "hgt"){
        return validateHgt(value); //cm 150 - 193 or in 59 - 76
    } else if(key == "hcl"){
        return validateHcl(value); //# followed by 6 characters of 0-9 or a-f
    } else if(key == "ecl"){
        return validateEcl(value); // is "amb, brn, gry, grn, hzl, oth"
    } else if(key == "pid"){
        return validatePid(value); // 9 digit number including 1 leading 0 
    } else if (key == "cid"){
        return 1;
    } else if (key == ""){
        return 1;
    }
    return 0;
}

int  validateHgt(string value){
    if (value.find("in") != -1){
        int size = stoi(value.substr(0,value.find("in")));
        return (59 <= size && size <= 76) ? 1 : 0;
    } 
    else if (value.find("cm") != -1){
        int size = stoi(value.substr(0,value.find("cm")));
        return (150 <= size && size <= 193) ? 1 : 0;
    }
    return 0;
}

int  validateHcl(string value){
    if (value[0] != '#' || value.length() != 7)
        return 0;

    for (int i = 1; i < value.length() ; i++){
        char c = value[i];
        if( !(isdigit(c) || ('a' <= c && c <= 'f')) )
            return 0;
    }
    return 1;
}
int  validateEcl(string value){
    return (value == "amb" || value == "blu" || value == "brn" || value == "gry" || value == "grn" || value == "hzl" || value == "oth") ? 1:0;
}
int  validatePid(string value){
    if (value.length() != 9)
        return 0;

    for (int i = 0; i < value.length() ; i++){
        if (!isdigit(value[i]))
            return 0;
    }
    return 1;
}

void printList(vector<string> items){
    cout << "items:\n";
    for(string item : items){
        cout << item << "\n[END OF ITEM]\n";
    }
}