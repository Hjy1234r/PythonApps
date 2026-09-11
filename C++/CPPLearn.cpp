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
#if 0
  int radius;
  cout << "Enter the radius: ";
  cin >> radius;
  cout << "The area of the circle is: "
       << pow(radius, 2) * numbers::pi << endl;
  cout << "The circumference of the circle is: "
       << 2*radius * numbers::pi << endl;
#endif
#if 0
  int first, second, temp;
  cout << "Input 1st number: ";
  cin >> first;
  cout << "Input 2nd number: ";
  cin >> second;
  temp = first;
  first = second;
  second = temp;
  cout << "First number: " << first << endl
       << "Second number: " << second << endl;
#endif

  // Chapter 3 Exercises:
  // Check whether a number is positive or negative, even or odd
#if 0
  int input;
  cout << "Enter a number: ";
  cin >> input;
  if (input > 0)
    cout << "Number is positive\n";
  else if (input < 0)
    cout << "Number is negative\n";
  else
    cout << "Number is zero\n";

  if (input % 2 == 0)
    cout << "Number is even\n";
  else
    cout << "Number is odd\n";
#endif
  // Find the largest number among three
#if 0
  int n1, n2, n3, max = 1;
  cout << "Enter 3 numbers: ";
  cin >> n1 >> n2 >> n3;
  if (n1 == n2 || n1 == n3 || n2 == n3)
    cout << "Two or three numbers are equal.\n";
  else if (n1 > n2) {
    if (n1 > n3)
      max = n1;
    else
      max = n3;
  } else {
    if (n2 > n3)
      max = n2;
    else
      max = n3;
  }
  cout << "The largest number is " << max << endl;
#endif
  // Solve first degree equation
#if 0
  double a, b, result;
  cout << "ax + b = 0\n" << "Enter the coefficients a and b: ";
  cin >> a >> b;
  if (a == 0 && b == 0)
    cout << "Infinite Solutions.\n";
  else if (a == 0 && b != 0)
    cout << "No Solution.\n";
  else {
    result = -b / a;
    cout << "X = " << result << endl;
  }
#endif
  // Check for a right triangle
#if 0
  double a, b, c;
  cout << "Enter three sides of a triangle: ";
  cin >> a >> b >> c;
  if (c == sqrt(a * a + b * b))
    cout << "It is a right triangle!\n";
  else if (a == sqrt(c * c + b * b))
    cout << "It is a right triangle!\n";
  else if (b == sqrt(a * a + c * c))
    cout << "It is a right triangle!\n";
  else
    cout << "It is not a right triangle.\n";
#endif

  // Check for number of days in a month and year
#if 0
  int month, year, days;
  bool is_leap;
  cout << "Enter the month and year: ";
  cin >> month >> year;
  if (year % 4 == 0 && year % 100 != 0)
    is_leap = true;
  else if (year % 100 == 0 && year % 400 == 0)
    is_leap = true;
  else
    is_leap = false;
  switch (month) {
  case 1:
    days = 31;
    break;
  case 2:
    if (is_leap)
      days = 29;
    else
      days = 28;
    break;
  case 3:
    days = 31;
    break;
  case 4:
    days = 30;
    break;
  case 5:
    days = 31;
    break;
  case 6:
    days = 30;
    break;
  case 7:
    days = 31;
    break;
  case 8:
    days = 31;
    break;
  case 9:
    days = 30;
    break;
  case 10:
    days = 31;
    break;
  case 11:
    days = 30;
    break;
  case 12:
    days = 31;
    break;
  default:
    cout << "Invalid month.\n";
  }
  cout << "Number of days: " << days << endl;
#endif
  return 0;
}