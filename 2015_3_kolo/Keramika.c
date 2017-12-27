#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int gcd(int a, int b) {
	int ost = a % b;
	while(ost > 0) {
		a = b;
		b = ost;
		ost = a % b;
	}
	return b;
}

int* tujaStevila(int n) {
	int *rez = (int *) malloc((n+1)*sizeof(int));
	rez++; // na -1. mesto shranimo dolzino :)
	int ind = 0;
	for(int i=1; i<n; ++i) {
		if(gcd(i, n) == 1) {
			rez[ind] = i;
			ind++;
		}
	}
	rez[ind] = -1;
	rez[-1] = ind;
	return rez;
}

int pozicija(int *sirina, int element) {
	int a = 0, b = sirina[-1]-1;
	if(sirina[b] < element) return b+1;
	while(b - a > 0) {
		int s = (a + b) / 2;
		if(sirina[s] >= element) {
			b = s;
		}
		else {
			a = s + 1;
		}
	}
	return a;
}

int main() {
	int w, h, a, b;
	scanf("%d %d %d %d", &w, &h, &a, &b);
	int *visina = tujaStevila(h);
	int *sirina = tujaStevila(w);
	int i=0;
	long long rez = 0;
	while(visina[i] > -1) {
		int miny = ceil((double)a / visina[i]);
		int maxy = b / visina[i] + 1;
		rez += (pozicija(sirina, maxy) - pozicija(sirina, miny));
		//printf("%lld\n", rez);
		i++;
	}
	printf("%lld\n", rez);
	free(--sirina);
	free(--visina);
	return 0;
}