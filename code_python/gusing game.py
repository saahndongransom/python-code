hidding_word = "python"
gust = ""
gust_count =0
gust_limit = 3
out_of_gusing = False
while gust != hidding_word:
    if gust_count < gust_limit and not (out_of_gusing):
        gust=input("enter a gust:")
        gust_count +=1
else:
    out_of_gusing = True
    if out_of_gusing:
        print("you lose")
    else:
        print("Congratulation")
