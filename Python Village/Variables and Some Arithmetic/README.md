<h2>Variables and Some Arithmeticclick to collapse</h2>
<div>
    <p>One of the most important features of any programming language is its ability to manipulate variables. A variable is just a name that refers to a value; you can think of a variable as a box that stores a piece of data.</p>
    <p>In&nbsp;<a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a>, the basic data types are strings and numbers. There are two types of numbers: integers (both positive and negative) and floats (fractional numbers with a decimal point). You can assign numbers to variables very easily. Try running the following program:</p>
    <div>
        <pre>a = 324
b = 24
c = a - b
print &apos;a - b is&apos;, c</pre>
    </div>
    <p>In the above code, a, b, and c are all integers, and &apos;a - b is&apos; is a string. The result of this program is to print:</p>
    <div>
        <pre>a - b is 300</pre>
    </div>
    <p>You can now use all common arithmetic operations involving numbers:</p>
    <ul>
        <li>Addition:&nbsp;<code>2 + 3 == 5</code></li>
        <li>Subtraction:&nbsp;<code>5 - 2 == 3</code></li>
        <li>Multiplication:&nbsp;<code>3 * 4 == 12</code></li>
        <li>Division:&nbsp;<code>15 / 3 == 5</code></li>
        <li>Division remainder:&nbsp;<code>18 % 5 == 3</code></li>
        <li>Exponentiation:&nbsp;<code>2 ** 3 == 8</code></li>
    </ul>
    <p>It is important to note that if you try to divide two integers,&nbsp;<a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a> always rounds&nbsp;<em>down</em> the result (so&nbsp;<code>18/5 == 3</code>).</p>
    <p>To obtain a precise result for this division, you need to indicate floating-point division; either of the following expressions results in a &quot;float&quot; data type:&nbsp;<code>18.0/5 == 3.6</code> or&nbsp;<code>float(18)/5 == 3.6</code></p>
    <p>In&nbsp;<a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a>, the single equals sign (<code>=</code>) means &quot;assign a value to a variable&quot;. For example,&nbsp;<code>a = 3</code> assigns 3 to the integer a. In order to denote equality,&nbsp;<a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a> uses the double equals sign (<code>==</code>).</p>
    <p>In&nbsp;<a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a>, a string is an ordered sequence of letters, numbers and other characters. You can create string variables just like you did with :</p>
    <div>
        <pre>a = &quot;Hello&quot;
b = &quot;World&quot;</pre>
    </div>
    <p>Notice that the string must be surrounded by &quot; or &apos; (but not a mix of both). You can use quotes inside the string, as long as you use the opposite type of quotes to surround the string, e.g.,&nbsp;<code>a = &quot;Monty Python&apos;s Flying Circus&quot;</code> or&nbsp;<code>b = &apos;Project &quot;Rosalind&quot;&apos;</code>.</p>
    <p>String operations differ slightly from operations on numbers:</p>
    <div>
        <pre>a = &apos;Rosalind&apos;
b = &apos;Franklin&apos;
c = &apos;!&apos;
print a + &apos; &apos; + b + c*3</pre>
    </div>
    <p>Output:</p>
    <div>
        <pre>Rosalind Franklin!!!</pre>
    </div>
</div>
<h2>Problem</h2>
<p>Given:&nbsp;Two positive integers&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">aa</span> and&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">bb</span>, each less than 1000.</p>
<p>Return:&nbsp;The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">a</span> and&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">b</span>.</p>
