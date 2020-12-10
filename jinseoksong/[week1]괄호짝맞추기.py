#1. 자바 결과: 실패 원인:
import java.io.*;
import java.util.*;
class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int a = 0;
		int b = 0; 
		int c = 0;
		int d = 0;
		int e = 0;
		int f = 0;
		String arr = sc.next();
		String array[];
    #// 배열에 한글자씩 넣어주는 코드
		array = arr.split("");
    #// 한 글자씩 숫자 비교해 주는 것
		for(int i = 0; i < array.length; i++){
			if(array[i].equals("(")){
				a++;
			}else if(array[i] == ")"){
				b++;
			}else if(array[i] == "{"){
				c++;
			}else if(array[i] == "}"){
				d++;
			}else if(array[i] == "["){
				e++;
			}else{
				f++;
			}
		}
    # 여기서 오류 난 것 같은데 이 식이 틀렸는가?
		if(a == b && c == d && e == f){
			System.out.print("Ture");
		}else {
			System.out.print("False");
		}
	}
}

#2. 파이썬 결과: 테스트못한케이스 원인: ?
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
input = input()
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
for i in input:
	if i == "{":
		a += 1
	elif i == "[":
		b += 1
	elif i == "(":
		c += 1
	elif i == ")":
		d += 1
	elif i == "}":
		e += 1
	else:
		f += 1
if a == e and b == f and c == d:
	print("True")
else:
	print("False")