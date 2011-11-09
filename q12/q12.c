#include <stdio.h>

int main()
{
	int i = 1;
	int count, n, x;
	while(1) {
		count = 0;
		n = i * (i+1) /2;
		for(x = 1; x < ceil(sqrt(n)); x++) {
			if(n %x == 0)
				count += 2;
		}
		if(count > 500)
			break;
		i++;
	}
	printf("number is %d\n", n);
}
