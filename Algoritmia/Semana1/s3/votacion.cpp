#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CANDIDATES 50
#define MAX_VOTERS 10000

int main() {
    int c, v;
    scanf("%d %d", &c, &v);

    int ballots[MAX_VOTERS][MAX_CANDIDATES];
    int eliminated[MAX_CANDIDATES + 1] = {0};
    int votes[MAX_CANDIDATES + 1];
    int remaining = c;

    for (int i = 0; i < v; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &ballots[i][j]);
        }
    }

    while (remaining > 0) {
        memset(votes, 0, sizeof(votes));

        for (int i = 0; i < v; i++) {
            for (int j = 0; j < c; j++) {
                int candidate = ballots[i][j];
                if (!eliminated[candidate]) {
                    votes[candidate]++;
                    break;
                }
            }
        }

        int winner = 0;
        for (int i = 1; i <= c; i++) {
            if (!eliminated[i] && votes[i] * 2 > v) {
                winner = i;
                break;
            }
        }

        if (winner) {
            printf("%d\n", winner);
            return 0;
        }

        int minVotes = v + 1;
        for (int i = 1; i <= c; i++) {
            if (!eliminated[i] && votes[i] < minVotes) {
                minVotes = votes[i];
            }
        }

        for (int i = 1; i <= c; i++) {
            if (!eliminated[i] && votes[i] == minVotes) {
                eliminated[i] = 1;
                remaining--;
            }
        }

        if (remaining == 0) {
            printf("0\n");
            return 0;
        }
    }

    printf("0\n");
    return 0;
}
