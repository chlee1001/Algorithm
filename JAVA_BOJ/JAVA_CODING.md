# Coding Test with JAVA

## 팁

- Scanner vs. BufferedReader

  ```java
  import java.util.Scanner;
  
  public class Scanner {
  	public static void main(String[] args) {
  		Scanner scanner = new Scanner(System.in);
  
  		System.out.println("원하는 숫자를 입력하세요");
  		String input = scanner.nextLine();
  		int num = Integer.parseInt(input);
  		System.out.println(num);
  	}
  }
  ```

  ```java
  import java.io.BufferedReader;
  import java.io.IOException;
  import java.io.InputStreamReader;
  
  public class Buffer {
  	public static void main(String[] args) throws IOException {
  		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
  		String s = br.readLine(); 
  		int i = Integer.parseInt(br.readLine()); 
  		
  		System.out.println("String : " + s);
  		System.out.println("Int : " + i);
  		
  	}
  }

![img](https://blog.kakaocdn.net/dn/bYIB07/btqw78Z308y/KsqnoZaTZlLkuQ0TeGhXe1/img.png)