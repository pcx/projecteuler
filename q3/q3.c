/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

http://projecteuler.net/problem=3
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct factor_node {
	long long int factor; //value of the factor
	long long int ppt_value; //precipitate value
	struct factor_node *next;
};

int check_if_prime(long long int num);
long long int get_next_prime(long long int ppt_value, long long int present_prime);
void factorise_node(struct factor_node *root);
void print_nodes(struct factor_node *root);
long long int get_largest_factor(struct factor_node *root);


int main()
{
	long long int ppt;
	printf("Please enter a number to be factorised:\t");
	scanf("%lld", &ppt);

	printf("Creating root node...");
	struct factor_node *root;
	root = (struct factor_node *) malloc(sizeof(struct factor_node));
	root->factor = 1;
	root->ppt_value = ppt;
	printf("Done\n\n");

	printf("Factorising nodes now...");
	factorise_node(root);
	printf("Done\n\n");
	
	printf("Printing all nodes:\n");
	print_nodes(root);

	printf("\nThe largest prime factor of %lld is %lld\n", ppt, get_largest_factor(root));
}

int check_if_prime(long long int num)
{
	if(num == 2)
		return(1);
	long long int present_divisor = 1;
	long long int upper_limit = ceil(sqrt(num));
	while(present_divisor < upper_limit) {
		present_divisor++;
		if(num % present_divisor == 0) {
			return(0);
		}
	}
	return(1);
}

long long int get_next_prime(long long int ppt_value, long long int present_prime)
{
	long long int upper_limit = ceil(sqrt(ppt_value));
	long long int i = present_prime;
	while(i < upper_limit) {
		i++;
		if(check_if_prime(i)) {
			break;
		}
	}
	if(present_prime == upper_limit)
		return(0);
	else
		return(i);
}

void factorise_node(struct factor_node *root)
{
	long long int present_prime = 1;
	while(1) {
		present_prime = get_next_prime(root->ppt_value, present_prime);
		if(present_prime == 0)
			break;
		if(root->ppt_value % present_prime == 0) {
			struct factor_node *next;
			next = (struct factor_node *) malloc(sizeof(struct factor_node));
			next->factor = present_prime;
			next->ppt_value = root->ppt_value / next->factor;
			root->next = next;
			break;
		}
	}
	if(root->next != '\0') {
		factorise_node(root->next);
	}
}

void print_nodes(struct factor_node *root)
{
	printf("%lld\t=\t%lld x %lld\n", root->factor*root->ppt_value, root->factor, root-> ppt_value);
	if(root->next != '\0')
		print_nodes(root->next);
}


long long int get_largest_factor(struct factor_node *root)
{
	long long int x, largest;
	largest = root->factor;
	if(root->next != '\0') {
		if((x=get_largest_factor(root->next)) > largest)
			largest = x;
	}
	else {
		if(root->ppt_value > largest)
			largest = root->ppt_value;
	}
	return(largest);
}
