main()
{  int count = 3;
　int i;
  for(i=0; i<2; i++) {
	fork();
	printf("count=%d\n", count);
	count++;
  }
}

