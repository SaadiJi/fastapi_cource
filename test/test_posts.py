from typing import List
from app import schemas

def test_get_all_posts(authorized_client,test_posts):
    res = authorized_client.get("/posts/")
    print(res.json())
    print("+++++++++++++++++++++++++++++++")
    print(test_posts)
    assert res.status_code == 200
    def validate(post):
        return schemas.PostOut(**post)
    
    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    assert posts_list[0].Post.id == test_posts[0].id
    
# def test_unauthorized_user_get_one_post(cleint, test_posts):
#     res = cleint.get(f"/posts/{test_posts[0].id}")
#     assert res.status_code == 401
    
# def test_get_one_psot_not_exist(authorized_client,test_posts):
#     res = authorized_client.get(f"/posts/88888")
#     assert res.status_code == 404
    
# def test_get_one_post(authorized_client, test_posts):
#     res = authorized_client.get(f"/posts/{test_posts[0].id}")
#     print(res.json())

