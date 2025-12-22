// Fizzbuzz
public class Solution {

    public static void main(String[] args) {
        for (int i = 1; i < 101; i++) {
            if (i % 3 < 1 && i % 5 < 1) {
                System.out.println("FizzBuzz");
            } else if (i % 5 < 1) {
                System.out.println("Buzz");
            } else if (i % 3 < 1) {
                System.out.println("Fizz");
            } else {
                System.out.println(i);
            }
            // System.out.println((i%3>0?"":"Fizz")+(i%5>0?i%3>0?i:"":"Buzz")));
        }
    }
}

// STring reverse
public class Solution {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        /* Enter your code here. Print output to STDOUT. */
        int start = 0;
        int end = A.length() - 1;
        int count = 0;

        // Sln 1
        // while (A.charAt(start) == A.charAt(end) && start++ < end-- );

        // System.out.println(start > end ? "Yes" : "No");

        // Sln 2
        // for (int i = start; i < A.length()/2; i++){
        // if (A.charAt(start) == A.charAt(end)){
        // count++;
        // }

        // }
        // Sln 3
        // System.out.println( (count == A.length()/2) ? "Yes" : "No") ;

        System.out.println(A.equals(new StringBuilder(A).reverse().toString()) ? "Yes" : "No");
    }
}

// Palindrome LC
class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int start = 0, end = s.length() - 1;
        while (start < end) {
            if (s.charAt(start++) != s.charAt(end--)) {
                return false;
            }
        }
        return true;
    }
}

// Anagram LC
class Solution {
    public boolean isAnagram(String s, String t) {
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            count[t.charAt(i) - 'a']--;
        }
        for (int i : count) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }

}

// Anagram HR
    static int anagram(String s) {
        int[] freq=new int[26];
        int n=s.length();
        int count=0;

        if(n%2!=0)
            return -1;

        for(int i=0;i<n/2;i++)
            freq[s.charAt(i)-'a']++;

        for(int i=n/2;i<n;i++)
            freq[s.charAt(i)-'a']--;

        for(int i=0;i<26;i++)
            count+=Math.abs(freq[i]);

        return count/2;
    }
