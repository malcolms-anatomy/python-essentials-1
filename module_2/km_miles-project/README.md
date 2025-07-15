# Scenario 1

Miles and kilometers are units of length or distance.

Bearing in mind that **1 mile is equal to approximately 1.61 kilometers**, complete the program in the editor so that it converts:

- miles to kilometers
- kilometers to miles

**Do not change anything in the existing code.**  
Write your code in the places indicated by `###`.  
Test your program with the data we've provided in the source code.

---

Pay particular attention to what is going on inside the `print()` function.  
Analyze how we provide multiple arguments to the function, and how we output the expected data.

Note that some of the arguments inside the `print()` function are strings (e.g., `"miles is"`), whereas others are variables (e.g., `miles`).

> **TIP:**  
> There's one more interesting thing happening there. Can you see another function inside the `print()` function?  
> It's the `round()` function. Its job is to round the outputted result to the number of decimal places specified in the parentheses, and return a float (inside the `round()` function you can find the variable name, a comma, and the number of decimal places we're aiming for).  
> We're going to talk about functions very soon, so don't worry that everything may not be fully clear yet.  
> We just want to spark your curiosity.

---

After completing the lab, open **Sandbox**, and experiment more.  
Try to write different converters, e.g., a USD to EUR converter, a temperature converter, etc. – let your imagination fly!  
Try to output the results by combining strings and variables.  
Try to use and experiment with the `round()` function to round your results to one, two, or three decimal places.  
Check out what happens if you don't provide any number of digits.  
Remember to test your programs.

Experiment, draw conclusions, and learn. **Be curious.**

---

## Expected output

```
7.38 miles is 11.88 kilometers
12.25 kilometers is 7.61
```

# Scenario 2

Take a look at the code in the editor: it reads a float value, puts it into a variable named `x`, and prints the value of a variable named `y`.  
Your task is to complete the code in order to evaluate the following expression:

```
3x³ - 2x² + 3x - 1
```

The result should be assigned to `y`.

> **Note:**  
> Classical algebraic notation likes to omit the multiplication operator — you need to use it explicitly in code.  
> Also, make sure that `x` is of type `float`.

Keep your code clean and readable, and test it using the data we've provided, each time assigning it to the `x` variable (by hardcoding it).  
Don't be discouraged by any initial failures. Be persistent and inquisitive.

---

## Test Data

**Sample input:**
```
x = 0
x = 1
x = -1
```

**Expected Output:**
```
y = -1.0
y = 3.0
y = -