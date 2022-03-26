#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::vector<std::string> makeLineGroups(std::vector<std::string> contents){
    std::vector<std::string> groups;
    groups.push_back("");
    for(std::vector<std::string>::iterator line = contents.begin(); line != contents.end(); ++line){
        if(*line==""){
            groups.push_back("");
            continue;
        }else{
            groups.back() += *line + " ";
        }
    }
    return groups;
}

void readFile(std::ifstream &myFileStream, std::vector<std::string> &items){
    for( std::string myString ; getline(myFileStream, myString) ; ){
        items.push_back(myString);
    }
}

std::vector<std::string> openAndReadFile(std::string input){
    std::ifstream myFileStream;
    std::vector<std::string> items;
    myFileStream.open(input);

    if( myFileStream.is_open() ){
        readFile(myFileStream, items);
    }else{
        std::cout << "File " << input << " couldn't open." << std::endl;
        exit(2);
    }
    myFileStream.close();
    return items;
}

void printVector(std::vector<std::string> items){
    std::cout << "items { ";
    for(std::string item : items){
        std::cout << item << ", ";
    }
    std::cout << "}; \n";
}

//nextWord(string)

//isNumber(string)

//trim(string)

std::string::iterator findNextLetter(std::string::iterator c){
    for(; isspace(*c) && *c != '\0'; c++);
    return c;
}

std::string::iterator findNextSpace(std::string::iterator c){
    for(; !isspace(*c) && *c != '\0'; c++);
    return c;
}

std::string::iterator findNextWord(std::string::iterator c){
    c = findNextSpace(c);

    c = findNextLetter(c);

    return c;
}

void trim(std::string &str){
    int strLength = str.length();

    int length = 0;

    std::string::iterator start;

    for(start = str.begin(); isspace(*start) && *start != '\0'; start++);

    str.erase(str.begin(), start);

    std::string::iterator end;

    for(end = str.end()-1; isspace(*end) && end != str.begin(); end--);

    end++; //goes one too far

    str.erase(end,str.end());
}

std::vector<std::string> getAllWords(std::string str){
    std::vector<std::string> words;
    trim(str);
    std::string::iterator point = str.begin();

    while(*point != '\0'){
        std::string::iterator first = findNextLetter(point);
        std::string::iterator second = findNextSpace(first);

        std::string word = std::string(first,second);

        words.push_back(word);
        
        point = second;
    }
    
    return words;
}

// std::string::iterator findNextWord(std::string &str, int start){
//     std::string::iterator  c;
//     for(c = str.begin() + start; !isspace(*c) && c != str.end(); c++);

//     c = findNextLetter(c, start);

//     return c;
// }

// int main(){
//     std::string test = "   test is a test";
//     std::cout << test << std::endl;
//     trim(test);
//     //std::vector<std::string> words = getAllWords(test);
    
//     // printVector(words);

//     // std::string first_word = test.substr(first, findNextSpace(test.begin()+first));

//     // int x = findNextWord(test, 0) - test.begin(); // 5

//     // int y = findNextWord(test, x) - (test.begin() + x); 

//     // test.erase(x, y);

//     std::cout << "$" << test << "$" << std::endl;
// }