# 0x06. Regular expression :page_facing_up: :bookmark_tabs:
---

## Description :newspaper:
This project was created with learning purposes at Holberton School; on `Ubuntu 14.04`; and is about `regular expressions` (or regex, regexp, ...).


---
### Background Context :mortar_board:
For this project, I have to build my regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the `//`:
    
    your@shell$ cat example.rb
    #!/usr/bin/env ruby
    puts ARGV[0].scan(/127.0.0.[0-9]/).join
    your@shell$
    your@shell$ ./example.rb 127.0.0.2
    127.0.0.2
    your@shell$ ./example.rb 127.0.0.1
    127.0.0.1
    your@shell$ ./example.rb 127.0.0.a

---
### Resources :blue_book: :orange_book: :green_book:
Read or watch:
- [Regular Expression](http://www.regular-expressions.info)
- [Learn Regular expressions with simple, interactive exercises](https://regexone.com)

---

### Tasks :white_check_mark:

##### 0. Simply matching Holberton 
![Holberton](https://scontent.fctg1-1.fna.fbcdn.net/v/t1.0-9/153244968_2924652737812401_7945017625243681032_o.jpg?_nc_cat=100&ccb=3&_nc_sid=730e14&_nc_ohc=yDefuGsf-3sAX8cg3_5&_nc_ht=scontent.fctg1-1.fna&oh=1275841c818353393d5754b0721047c3&oe=6057D382 "Holberton")
The regular expression must match `Holberton`

##### 1. Repetition Token #0 
![hbtn](https://scontent.fctg1-1.fna.fbcdn.net/v/t1.0-9/153550349_2924652774479064_7584678069256865803_o.jpg?_nc_cat=105&ccb=3&_nc_sid=730e14&_nc_ohc=F0elwTDKNwcAX-OHPul&_nc_ht=scontent.fctg1-1.fna&oh=316dc67d3ac41198ec4e88d2483b949e&oe=605834A1)
Find the regular expression that will match the above cases

##### 2. Repetition Token #1
![htn](https://scontent.fctg1-2.fna.fbcdn.net/v/t1.0-9/153168395_2924652801145728_8456957351970911144_o.jpg?_nc_cat=107&ccb=3&_nc_sid=730e14&_nc_ohc=sF-9WVbDni0AX9eJF9w&_nc_ht=scontent.fctg1-2.fna&oh=aed14bb065559d83ab23ee5e2dcc8673&oe=605A2C5D)
Find the regular expression that will match the above cases

##### 3. Repetition Token #2
![hbttttn](https://scontent.fctg1-2.fna.fbcdn.net/v/t1.0-9/153089629_2924652857812389_1745875618219054663_o.jpg?_nc_cat=106&ccb=3&_nc_sid=730e14&_nc_ohc=VNPj9l138zsAX9biImu&_nc_ht=scontent.fctg1-2.fna&oh=a93b3d12fef5c2f86afeea27d63f505f&oe=605ADEBF)
Find the regular expression that will match the above cases

##### 4. Repetition Token #3
![hbn hbttttn](https://scontent.fctg1-1.fna.fbcdn.net/v/t1.0-9/153511222_2924652927812382_6468764862922204801_o.jpg?_nc_cat=100&ccb=3&_nc_sid=730e14&_nc_ohc=BVkwoA7prAwAX9Y1v4F&_nc_ht=scontent.fctg1-1.fna&oh=81c8df474e3cfda6390e66e0624448f5&oe=605B2D1D)
Find the regular expression that will match the above cases

##### 5. Not quite HBTN yet mandatory
The regular expression must be exactly matching a string that starts with `h` ends with `n` and can have any single character in between

##### 6. Call me maybe
The regular expression must match a 10 digit phone number

---

## Author
- [Adrian Vides] | [Twitter] | [GitHub]



---

[GitHub]: <https://github.com/AdrianVides56>
[Twitter]: <https://twitter.com/termi56661>
[Adrian Vides]: <https://www.linkedin.com/in/adrian-felipe-vides-jimenez-a201401b7> 
