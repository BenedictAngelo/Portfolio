# include <stdio.h>
# include <string.h>

int main() {
  
  // Shopping cart program

  char item[50] = "";
  float price = 0.0f;
  int quantity = 0;
  char currency = '$';
  float total = 0.0f;

  printf("What item would you like to buy? \n");
  fgets(item, sizeof(item), stdin);
  item[strlen(item) -1] = '\0';

  printf("What is the price for each? \n");
  scanf("%f", &price);

  printf("How many would you like? \n");
  scanf("%d", &quantity);

  total = price * quantity;
  printf("You have bought: \n%d %s/s", quantity, item);
  
  printf("\nWith the amount of: \n");
  printf("%c%.2f",currency, total);












  return 0;
}
