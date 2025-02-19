#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
int main(){
	setlocale(LC_ALL, "Portuguese_Brazil");
	
	int media, freq;
	
	printf("Digite a sua média:");
	scanf("%d",&media);
	
	printf("Digite sua frequência:");
	scanf("%d", &freq);
	
	if (media >= 6.0 && freq>= 75){
		printf("Você passou");
		
	}else if (media < 6 && freq >= 75){
		printf("Você está de exame");		
	}else {
		printf("Reprovado");
	}
	
	
	
	return 0;
}
