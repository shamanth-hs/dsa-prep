/**
 * Google Log Truncation Problem:
 * There is a logging system kept inside a machine. Which logs all the logs and saves in a file.
Truncate the logs with fair manner and save it.

Class Logs{
String filename;
String log;
}

Max = 30
List<Logs>

Output:
A: 15
B: 10
C: 5


Input : A: 50, B: 20, C: 5  size = 30

Output: A:12, B:13,C:5

A:”SOme log”
B:”log2”
C:”Log”
A:”SOme l”
C:lslsa”
A:”asd”












 */


#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

class LogTruncator {
private:
    const int MAX_TOTAL = 30;
    int currentTotal = 0;
    
    // Tracks count per filename/source
    std::unordered_map<std::string, int> usageMap;

public:
    void processLog(const std::string& source) {
        // 1. Check if the entire machine is full
        if (currentTotal >= MAX_TOTAL) {
            return; 
        }

        // Initialize source if it's the first time we see it (D, E, F...)
        if (usageMap.find(source) == usageMap.end()) {
            usageMap[source] = 0;
        }

        int sourceCount = usageMap[source];
        int numSources = usageMap.size();
        
        // 2. Calculate the fair share based on current unique sources
        // Using double for precision, then floor/cast for the limit
        int fairShare = MAX_TOTAL / numSources;

        /* Logic for "A:12, B:13, C:5":
           - C only takes 5.
           - A and B are allowed to exceed the 'fairShare' (10) 
             because the global 'currentTotal' hasn't hit 30 yet.
        */
        if (sourceCount < fairShare || currentTotal < MAX_TOTAL) {
            usageMap[source]++;
            currentTotal++;
            std::cout << "Saved " << source << " | Global: " << currentTotal << std::endl;
        }
    }

    void printFinalStats() {
        std::cout << "\n--- Final Allocation ---" << std::endl;
        for (const auto& pair : usageMap) {
            std::cout << pair.first << ": " << pair.second << std::endl;
        }
    }
};

int main() {
    LogTruncator tracker;

    // Simulated stream: A and B are heavy, C is light, D appears later
    std::vector<std::string> stream = {
        "A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C", // C hits 5 here
        "A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A", // A and B flooding
        "D", "E", "F" // These arrive but system might be full
    };

    for (const std::string& s : stream) {
        tracker.processLog(s);
    }

    tracker.printFinalStats();

    return 0;
}