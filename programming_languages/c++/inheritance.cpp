#include <iostream>

using namespace std;


class BaseExample {
    // Not inheritable, and not externally visible
    private:
        string secret;

    // Inheritable, but not externally visible
    protected:
        string str;

    // Inheritable, and externally visible
    public:
        BaseExample() {
            this->secret = "Shhh";
            this->str = "BaseExample";
        }

        ~BaseExample() {
            cout << "~" << this->str << " (Base)" << endl;
        }

        string getStr() const {
            return this->str;
        }
};


class DerivedExample : public BaseExample {
    public:
        DerivedExample() {
            this->str = "DerivedExample";
        }

        ~DerivedExample() {
            cout << "~" << this->str << " (Derived)" << endl;
        }
};


int main() {
    BaseExample base;
    DerivedExample derived;
    BaseExample &other = derived;       // Allowed because BaseExample is publicly inherited

    cout << base.getStr() << endl;
    cout << derived.getStr() << endl;
    cout << other.getStr() << endl;
    return 0;
}
