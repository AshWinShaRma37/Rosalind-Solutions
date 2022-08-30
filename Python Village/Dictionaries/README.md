
   <h2>Intro to Python dictionary</h2>
    <div>
        <p>We&apos;ve already used lists and strings to store and process data. Python also has a variable type called a &quot;dictionary&quot; that is similar to a list, but instead of having integer indices, you provide your own index, called a &quot;key&quot;. You can assign data to a dictionary as follows:&nbsp;<code>phones = {&apos;Zoe&apos;:&apos;232-43-58&apos;, &apos;Alice&apos;:&apos;165-88-56&apos;}</code>. We can therefore think of a dictionary as a &quot;function&quot; that maps a collection of keys to values. As with lists, the values of the list can be of any type: strings, integers, floating point numbers, even lists or dictionaries themselves. For keys you can use only strings, numbers, floats and other immutable types. Accessing values of a dictionary is also similar to accessing values of a list:</p>
        <div>
            <pre>phones = {&apos;Zoe&apos;:&apos;232-43-58&apos;, &apos;Alice&apos;:&apos;165-88-56&apos;}
print phones[&apos;Zoe&apos;]</pre>
        </div>
        <p>Here, the output should be:</p>
        <div>
            <pre>232-43-58</pre>
        </div>
        <p>Adding new values to a dictionary or assigning a new value to an existing key can be done as follows:</p>
        <div>
            <pre>phones[&apos;Zoe&apos;] = &apos;658-99-55&apos;
phones[&apos;Bill&apos;] = &apos;342-18-25&apos;
print phones</pre>
        </div>
        <p>This should produce the following:</p>
        <div>
            <pre>{&apos;Bill&apos;: &apos;342-18-25&apos;, &apos;Zoe&apos;: &apos;658-99-55&apos;, &apos;Alice&apos;: &apos;165-88-56&apos;}</pre>
        </div>
        <p>Note that the new&nbsp;<code>&apos;Bill&apos;</code> appeared in the beginning of the dictionary, not in the end, as you might expect. Dictionaries do not have an obvious ordering.</p>
        <p>Remember that dictionaries are case-sensitive if you are using strings as keys. For example, &apos;key&apos; and &apos;Key&apos; are viewed as different keys:</p>
        <div>
            <pre>d = {}
d[&apos;key&apos;] = 1
d[&apos;Key&apos;] = 2
d[&apos;KEY&apos;] = 3
print d</pre>
        </div>
        <p>Output:</p>
        <div>
            <pre>{&apos;KEY&apos;: 3, &apos;Key&apos;: 2, &apos;key&apos;: 1}</pre>
        </div>
        <p>Note how we created an empty dictionary with&nbsp;<code>d = {}</code>. This could be useful in case you need to add values to dictionary dynamically (for example, when reading a file). If you need to check whether there a key in dictionary, you can use&nbsp;<code>key in d</code> syntax:</p>
        <div>
            <pre>if &apos;Peter&apos; in phones:
    print &quot;We know Peter&apos;s phone&quot;
else:
    print &quot;We don&apos;t know Peter&apos;s phone&quot;</pre>
        </div>
        <p>Output:</p>
        <div>
            <pre>We don&apos;t know Peter&apos;s phone</pre>
        </div>
        <p>In case you need to delete a value from a dictionary, use the&nbsp;<code>del</code> command:</p>
        <div>
            <pre>phones = {&apos;Zoe&apos;:&apos;232-43-58&apos;, &apos;Alice&apos;:&apos;165-88-56&apos;}
del phones[&apos;Zoe&apos;]
print phones</pre>
        </div>
        <p>This produces the following output:</p>
        <div>
            <pre>{&apos;Alice&apos;: &apos;165-88-56&apos;}</pre>
        </div>
    </div>
<h2>Problem</h2>
<p>Given:&nbsp;A string&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">ss</span> of length at most 10000 letters.</p>
<p>Return:&nbsp;The number of occurrences of each word in&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">ss</span>, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.</p>
<h2>Sample Dataset</h2>
<div>
    <pre>We tried list and we tried dicts also we tried Zen</pre>
</div>
<h2>Sample Output</h2>
<div>
    <pre>and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1</pre>
</div>
    <h2>Hints</h2>
    <div>
        <p>To iterate over the words in a string, you can split it at each occurrence of empty space as follows:</p>
        <div>
            <pre>for word in str.split(&apos; &apos;):
    print word</pre>
        </div>
        <p>For a pretty representation when outputting a dictionary, you can use the built in&nbsp;<code>.items()</code> function:</p>
        <div>
            <pre>for key, value in dict.items():
    print key
    print value</pre>
        </div>
    </div>
