#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>

int main() {
    int numeroComputador, tentativaUsuario;
    
    // Inicializa a semente do gerador de números aleatórios
    srand(time(NULL));
    
    // Gera um número aleatório entre 1 e 6
    numeroComputador = (rand() % 6) + 1;
    
    // Solicita um palpite ao usuário
    printf("Tente adivinhar o número (entre 1 e 6): ");
    scanf("%d", &tentativaUsuario);
    
    // Verifica se o usuário acertou
    if (tentativaUsuario == numeroComputador) {
        printf("Parabéns! Você acertou, o número era %d.\n", numeroComputador);
    } else {
        printf("Você errou! O número correto era %d.\n", numeroComputador);
    }
    
    return 0;
}
