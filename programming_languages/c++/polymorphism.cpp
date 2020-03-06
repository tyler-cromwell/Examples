#include <iostream>

using namespace std;


class Animal {
    public:
        virtual ~Animal() {
            cout << "~Animal" << endl;
        }

        // Prevents derived override from being used through base type
        void speak_novirt() const {
            cout << "Sound. (no virtual)" << endl;
        }

        // Allows derived override to be used through base type
        virtual void speak_virt() const {
            cout << "Sound.. (virtual)" << endl;
        }

        // Must be overidden/implemented by derived classes
        virtual string species() const = 0;
};


class Bird : public Animal {
    public:
        // Not called implicitly through base class type unless base destructor is virtual
        ~Bird() {
            cout << "~Bird" << endl;
        }

        void speak_novirt() const {
            cout << "Tweet! Tweet! (no virtual)" << endl;
        }

        void speak_virt() const {
            cout << "Tweet! Tweet! (virtual)" << endl;
        }

        string species() const {
            return "Bird";
        }
};


class Dog : public Animal {
    public:
        // Not called implicitly through base class type unless base destructor is virtual
        ~Dog() {
            cout << "~Dog" << endl;
        }

        void speak_novirt() const {
            cout << "Woof! (no virtual)" << endl;
        }

        void speak_virt() const {
            cout << "Woof! (virtual)" << endl;
        }

        string species() const {
            return "Dog";
        }
};


int main() {
    Animal *bird = new Bird();  // Allowed because Animal is publicly inherited
    Animal *dog = new Dog();    // Allowed because Animal is publicly inherited

    bird->speak_novirt();
    dog->speak_novirt();

    bird->speak_virt();
    dog->speak_virt();

    cout << bird->species() << endl;
    cout << dog->species() << endl;

    delete bird;
    delete dog;
    return 0;
}
