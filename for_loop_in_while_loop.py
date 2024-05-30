#--------------------#
blog_post = []
while len(blog_post) < 5:
    comment = input("Can you blog with an inspirational Quote!\n")
    blog_post.append(comment)


for post in blog_post:
    if post == "":
        continue
    else:
        print(post)
