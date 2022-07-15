<h2>Strings and listsc</h2>
<div>
    <p>We&apos;ve already seen numbers and strings, but <a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a> also has variable types that can hold more than one piece of data at a time. The simplest such variable is a list.</p>
    <p>You can assign data to a list in the following way: <code>list_name = [item_1, item_2, ..., item_n]</code>. The items of the list can be of any other type: integer, float, string. You even explore your inner Zen and make lists of lists!</p>
    <p>Any item in a list can be accessed by its index, or the number that indicates its place in the list. For example, try running the following code:</p>
    <div>
        <pre>tea_party = [&apos;March Hare&apos;, &apos;Hatter&apos;, &apos;Dormouse&apos;, &apos;Alice&apos;]
print tea_party[2]</pre>
    </div>
    <p>Your output should be:</p>
    <div>
        <pre>Dormouse</pre>
    </div>
    <p>Note that the output was <em>not</em> <code>Hatter</code>, as you might have guessed. This is because in <a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a>, indexing begins with 0, not 1. This property is called 0-based numbering, and it&apos;s shared by many programming languages.</p>
    <p>You can easily change existing list items by reassigning them. Try running the following:</p>
    <div>
        <pre>tea_party[1] = &apos;Cheshire Cat&apos;
print tea_party</pre>
    </div>
    <p>This code should output the list with &quot;Hatter&quot; replaced by &quot;Cheshire Cat&quot;:</p>
    <div>
        <pre>March Hare, Cheshire Cat, Dormouse, Alice</pre>
    </div>
    <p>You can also add items to the end of an existing list by using the function <code>append()</code>:</p>
    <div>
        <pre>tea_party.append(&apos;Jabberwocky&apos;)
print tea_party</pre>
    </div>
    <p>This code outputs the following:</p>
    <div>
        <pre>March Hare, Cheshire Cat, Dormouse, Alice, Jabberwocky</pre>
    </div>
    <p>If you need to obtain only some of a list, you can use the notation <code>list_name[a:b]</code> to get only those from the index <code>a</code> up to but <em>not</em> including index <code>b</code>. For example, <code>tea_party[1:3]</code> returns <code>Cheshire Cat, Dormouse</code>, not <code>Cheshire Cat, Dormouse, Alice</code>. This process is called &quot;list slicing&quot;.</p>
    <p>If the first index of the slice is unspecified, then <a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a> assumes that the slice begins with the beginning of the list (i.e., index 0); if the second index of the slice is unspecified, then you will obtain the items at the end of the list. For example, <code>tea_party[:2]</code> returns <code>March Hare, Cheshire Cat</code> and <code>tea_party[3:]</code> returns <code>Alice, Jabberwocky</code>.</p>
    <p>You can also use negative indices to count items backtracking from the end of the list. So <code>tea_party[-2:]</code> returns the same output as <code>tea_party[3:]</code>: <code>Alice, Jabberwocky</code>.</p>
    <p>Finally, <a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a> equips you with the magic ability to slice strings the same way that you slice lists. A string can be considered as a list of characters, each of which having its own index starting from 0. For example, try running the following code:</p>
    <div>
        <pre>a = &apos;flimsy&apos;
b = &apos;miserable&apos;
c = b[0:1] + a[2:]
print c</pre>
    </div>
    <p>This code will output the string formed by the first character of <code>miserable</code> and the last four characters of <code>flimsy</code>:</p>
    <div>
        <pre>mimsy</pre>
    </div>
</div>
<h2>Problem</h2>
<p>Given: A string <span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">ss</span> of length at most 200 letters and four integers <span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">aa</span>, <span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">bb</span>, <span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">cc</span> and <span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">dd</span>.</p>
<p>Return: The slice of this string from indices <span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">aa</span> through <span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">bb</span> and <span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">cc</span> through <span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">dd</span> (with space in between), <em>inclusively</em>. In other words, we should include elements <span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi><mo stretchy="false">[</mo><mi>b</mi><mo stretchy="false">]</mo></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">s[b]s[b]</span> and <span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi><mo stretchy="false">[</mo><mi>d</mi><mo stretchy="false">]</mo></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">s[d]s[d]</span> in our slice.</p>
<h2>Sample Dataset</h2>
<div>
    <pre>HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102</pre>
</div>
<h2>Sample Output</h2>
<div>
    <pre>Humpty Dumpty</pre>
</div>
