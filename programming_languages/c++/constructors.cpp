#include <iostream>

using namespace std;


class Example {
    private:
        string str;

    public:
        Example() {
            this->str = "Default";
        }

        Example(const string &s) {
            this->str = s;
        }

        // Copy constructor
        Example(const Example &other) {
            this->str = other.str;
        }

        // Move constructor
        Example(Example &&source) {
            this->str = move(source.str);
        }

        string getStr() const {
            return this->str;
        }
};


int main() {
    Example e1;
    cout << "e1: " << e1.getStr() << endl;

    Example e2("Example 2");
    cout << "e2: " << e2.getStr() << endl;

    Example e3(e2);
    cout << "e3: " << e3.getStr() << endl;

    Example e4("Example 4");
    cout << "e4: " << e4.getStr() << endl;

    Example e5(move(e4));
    cout << "e5: " << e5.getStr() << endl;
    cout << "e4: " << e4.getStr() << endl;
    return 0;
}
