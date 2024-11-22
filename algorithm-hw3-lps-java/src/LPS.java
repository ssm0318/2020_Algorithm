import java.util.Scanner;

public class LPS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();

        System.out.println(findLPS(str, reverse(str)));
    }

    static String reverse(String str) {
        StringBuilder stringBuilder = new StringBuilder();
        char[] strArr = str.toCharArray();

        for (int i = strArr.length; i > 0; i--) {
            stringBuilder.append(strArr[i - 1]);
        }

        return stringBuilder.toString();
    }

    static boolean isPair(char x, char y) {
        String str = "" + x + y;
        return ((str.contains("A") && str.contains("T")) ||
                (str.contains("C") && str.contains("G")));
    }

    static String findLPS(String str1, String str2) {
        if (str1.length() < 2) {
            return "";
        }

        int N = str1.length();
        int M = str2.length();
        char[] arr1 = str1.toCharArray();
        char[] arr2 = str2.toCharArray();
        int[][] table = new int[N + 1][M + 1];

        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= M; j++) {
                if (i == 0 || j == 0) {
                    table[i][j] = 0;
                } else if (isPair(arr1[i - 1], arr2[j - 1])) {
                    table[i][j] = table[i - 1][j - 1] + 1;
                } else {
                    table[i][j] = Math.max(table[i - 1][j], table[i][j - 1]);
                }
            }
        }

        int idx = table[N][M];
        char[] LPSArr = new char[idx + 1];

        int x = N, y = M;
        while (x > 0 && y > 0) {
            if (isPair(arr1[x - 1], arr2[y - 1])) {
                LPSArr[idx - 1] = arr1[x - 1];
                x--;
                y--;
                idx--;
            } else if (table[x - 1][y] > table[x][y - 1]) {
                x--;
            } else {
                y--;
            }
        }

        StringBuilder stringBuilder = new StringBuilder();
        for (char ch : LPSArr) {
            stringBuilder.append(ch);
        }
        return stringBuilder.toString();
    }
}
