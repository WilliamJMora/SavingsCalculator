# SavingsCalculator
Differential Equations Savings Calculators

**Abstract**

  In differential equations, students encounter modeling problems which they learn how to solve using systems of differential equations. Two examples of these models are predator versus prey and savings. In predator versus prey models, the two entities exist in an environment and the quantities of each of the animals affect each other. If there are too many predators, eventually the prey will become so scarce, the predators will start to die out until the prey population can regrow. In the savings models, a bank account with an interest rate is modeled to calculate a number of scenarios. This calculator has three different computations that can be used to find what the user needs or wants to know.

**Introduction**

  The purpose of this calculator is to help people setup their future savings goals. The calculator uses differential equations models to solve three different computations. The first calculator finds the time it will take for a bank account to reach a goal. The inputs it receives are the goal amount, interest rate, deposit and frequency, and the current balance. The second calculator returns how much money the user will need to deposit at a weekly rate to reach a goal in the allotted time. The user puts in the goal, interest rate, the length of time of reach the goal, and the current balance of the account. The third calculator, unlike the other two, does not have a goal. It finds how much money will be in an account after a period of time. The user types in the interest rate of the account, the length of time the user will save, the contribution frequency, and the current balance.

**Differential Equations Examples**

  This goes over an example from differential equations of each of the three calculators. The first problem is looking to find the time it will take to reach the user’s goal. The second problem goes over a problem looking for the deposit to reach a goal in a given time. The last problem finds the amount of money in an account after a given time.

  1.  There is an initial condition (current balance) of $2,000. The account has a 4% interest rate.  $50 is deposited per week and the goal is $15,000. How much time would it take to reach the goal?

  Differential equation for the amount of money in the account as a function of time *t* with the initial condition:

  <img width="598" alt="Formula1" src="https://github.com/WilliamJMora/SavingsCalculator/assets/116101032/e441632c-eab8-4a8b-8475-c1ed9d72e15b">


  2. If the goal from problem 1 is wanted in 2 years instead of 4.43, how much money would need to be deposited each week?

  <img width="576" alt="Formula2" src="https://github.com/WilliamJMora/SavingsCalculator/assets/116101032/b62a288f-55fa-40a8-a6c0-83fdfa30b801">


  3. There is an initial condition of $400. The account has an interest rate of 1.1%. $20 is deposited per week. How much money would be in the account after 4 years?

  <img width="497" alt="Formula3" src="https://github.com/WilliamJMora/SavingsCalculator/assets/116101032/8fac3599-7301-439f-9047-697704e38e3a">

**Application / Calculator Examples**

  The front-end application was created with HTML, CSS, and JavaScript. It consists of 4 pages. The main page is the menu showing the three types of calculators. The buttons below correspond with the labeled calculators and takes the user to the page to use that calculator. On each page, the user can type in the needed information into text boxes and utilize the dropdown menus for even more calculations. Once the user has clicked the submit button, the information provided by the user is given to a JavaScript function called calculate(). This turns each number or other type of information into a variable of type number or string. If the user types in a dollar sign or a comma, they are removed so the number can be properly converted into the number data type. The result will appear in the gray bar below the submit button. Here are screenshots of the calculators working given the examples in the previous section:

  Question 1:

  <img width="274" alt="Picture1" src="https://github.com/WilliamJMora/SavingsCalculator/assets/116101032/f2e49b22-98ec-4828-abfa-19bf73502d53">

  Question 2:

  <img width="339" alt="Picture2" src="https://github.com/WilliamJMora/SavingsCalculator/assets/116101032/900f7adf-8aeb-4e24-8ac7-fca213a56651">

  Question 3:

  <img width="302" alt="Picture3" src="https://github.com/WilliamJMora/SavingsCalculator/assets/116101032/d1e77488-e721-4d8e-a3cb-8c3d7a5157da">

**In Python**

  The calculator was originally programmed in Python and then translated into JavaScript. Here are the same examples as above in PyCharm:

  Question 1:

  <img width="378" alt="Python1" src="https://github.com/WilliamJMora/SavingsCalculator/assets/116101032/b60d8de2-4a30-4103-9954-168d15c3da40">

  Question 2:

  <img width="569" alt="Python2" src="https://github.com/WilliamJMora/SavingsCalculator/assets/116101032/4b14245a-43ce-44b7-bce7-424f8dcbb7e4">

  Question 3:

  <img width="610" alt="Python3" src="https://github.com/WilliamJMora/SavingsCalculator/assets/116101032/68c804ed-3799-4b27-abb2-4d3939010cc2">
  
