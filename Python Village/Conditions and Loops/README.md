<h2>Conditions and Loops</h2>
<div>
    <p>If you need&nbsp;<a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a> to choose between two actions, then you can use an&nbsp;<code>if</code>/<code>else</code> statement. Try running this example code:</p>
    <div>
        <pre>a = 42
if a &lt; 10:
  print &apos;the number is less than 10&apos;
else:
  print &apos;the number is greater or equal to 10&apos;</pre>
    </div>
    <p>Note the indentation and punctuation (especially the colons), because they are important.</p>
    <p>If we leave out an, then the program continues on. Try running this program with different initial values of&nbsp;<code>a</code> and&nbsp;<code>b</code>:</p>
    <div>
        <pre>if a + b == 4:
  print &apos;printed when a + b equals four&apos;
print &apos;always printed&apos;</pre>
    </div>
    <p>If you want to repeat an action several times, you can use a while loop. The following program prints&nbsp;<code>Hello</code> once, then adds 1 to the&nbsp;<code>greetings</code> counter. It then prints&nbsp;<code>Hello</code> twice because&nbsp;<code>greetings</code> is equal to 2, then adds 1 to&nbsp;<code>greetings</code>. After printing&nbsp;<code>Hello</code> three times,&nbsp;<code>greetings</code> becomes 4, and the&nbsp;<code>while</code> condition of&nbsp;<code>greetings &lt;= 3</code> is no longer satisfied, so the program would continue past the&nbsp;<code>while</code> loop.</p>
    <div>
        <pre>greetings = 1
while greetings &lt;= 3:
  print &apos;Hello! &apos; * greetings
  greetings = greetings + 1</pre>
    </div>
    <p>Be careful! If you accidentally create an infinite loop, your program will freeze and you will have to abort it. Here&apos;s an example of an infinite loop. Make sure you see why it will never exit the&nbsp;<code>while</code> loop:</p>
    <div>
        <pre>greetings = 1
while greetings &lt;= 3:
  print &apos;Hello! &apos; * greetings
  greetings = greetings + 0 # Bug here</pre>
    </div>
    <p>If you want to carry out some action on every element of a list, the&nbsp;<code>for</code> loop will be handy</p>
    <div>
        <pre>names = [&apos;Alice&apos;, &apos;Bob&apos;, &apos;Charley&apos;]
for name in names:
  print &apos;Hello, &apos; + name</pre>
    </div>
    <p>And if you want to repeat an action exactly&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">nn</span> times, you can use the following template:</p>
    <div>
        <pre>n = 10
for i in range(n):
  print i</pre>
    </div>
    <p>In the above code,&nbsp;<code>range</code> is a function that creates a list of integers between&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">00</span> and&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">nn</span>, where&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">nn</span> is not included.</p>
    <p>Finally, try seeing what the following code prints when you run it:</p>
    <div>
        <pre>print range(5, 12)</pre>
    </div>
    <p>More information about loops and conditions can be found&nbsp;<a href="http://docs.python.org/2/tutorial/controlflow.html" target="_blank">in the Python documentation</a>.</p>
</div>
<h2>Problem</h2>
<p>Given:&nbsp;Two positive integers&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">aa</span> and&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">bb</span> (<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo><</mo><mi>b</mi><mo><</mo><mn>10000</mn></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">a&lt;b&lt;10000a&lt;b&lt;10000</span>).</p>
<p>Return:&nbsp;The sum of all odd integers from&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">aa</span> through&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">bb</span>, inclusively.</p>
<h2>Sample Dataset</h2>
<div>
    <pre>100 200</pre>
</div>
<h2>Sample Output</h2>
<div>
    <pre>7500</pre>
</div>

<h2>Hint</h2>
    <div>
        <p>You can use&nbsp;<code>a % 2 == 1</code> to test if a is odd.</p>
    </div>
