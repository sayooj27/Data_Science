#include<stdio.h>
int main()
{
int a[100],n,item,pos,i;
printf("enter the number of elements:");
scanf("%d",&n);
printf("enter the elements:/n");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
printf("enter the element to insert:");
scanf("%d",&item);
printf("enter the position:");
scanf("%d",&pos);
for(i=n;i>=pos;i--)
{
a[i]=a[i-1];
}
a[pos-1]=item;
n++;
printf("array after insertion:/n");
for(i=0;i<n;i++)
{
printf("%d",a[i]);
}
return 0;
}
