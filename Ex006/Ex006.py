# include<stdio.h>
# include<stdbool.h>
# include<malloc.h>

int
solution(int
n, int ** ratings) {
                   // Write
your
code
here

}

int
main()
{
    int
n;
scanf("%d", & n);
int
i_ratings, j_ratings;
int ** ratings = (int **)
malloc((n) * sizeof(int *));
for (i_ratings = 0; i_ratings < n; i_ratings++)
{
    ratings[i_ratings] = (int *)
malloc((2) * sizeof(int));
}
for (i_ratings = 0; i_ratings < n; i_ratings++)
{
for (j_ratings = 0; j_ratings < 2; j_ratings++)
{
scanf("%d", & ratings[i_ratings][j_ratings]);
}
}

int out_ = solution(n, ratings);
printf("%d", out_);
}