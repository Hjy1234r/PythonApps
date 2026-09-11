#include <cmath>
#include <iomanip>
#include <iostream>
#include <numbers>
using namespace std;

int main() {
  // Chapter 2 Exercises:
#if 0
  int inputA, inputB;
  cout << "Enter two numbers: ";
  cin >> inputA >> inputB;
  cout << "Addition: " << inputA + inputB << endl
       << "Subtraction: " << inputA - inputB << endl
       << "Multiplication: " << inputA * inputB << endl
       << "Division: " << inputA / inputB << endl
       << "Modulus: " << inputA % inputB << endl;
#endif
#if 0
  int A, B;
  cout << "Enter two numbers: ";
  cin >> A >> B;
  cout << "The answer is: " << pow(A, 2) - pow(B, 2) << endl;
#endif
#if 0
  int A, B;
  cout << "Side 1: ";
  cin >> A;
  cout << "Side 2: ";
  cin >> B;
  cout << "The hypotenuse of the right triangle is: " << fixed
       << setprecision(2) << sqrt(pow(A, 2) + pow(B, 2)) << endl;
#endif
#if 1
  int radius;
  cout << "Enter the radius: ";
  cin >> radius;
  cout << "The circumference of the circle is: "
       << pow(radius, 2) * std::numbers::pi << endl;
#endif
  return 0;
}