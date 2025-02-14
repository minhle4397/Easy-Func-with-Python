"""
####  CMS Selector Based on a Given String  ####

Write a function that takes a list of strings and a pattern (string) and returns the strings that contain the pattern in alphabetical order. If the pattern is an empty string, return all the strings passed in the input list.


[Examples]

___
cms_selector(["WordPress", "Joomla", "Drupal"], "w") ➞ ["WordPress"]

cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "ru") ➞ ["Drupal"]

cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "") ➞ ["Drupal", "Joomla", "Magento", "WordPress"]
_____



[Notes]

___
*) The given letter(s) are case insensitive and can be more than one.
*) In the case of an empty string, return the entire list.
*) A CMS is a Content Management System.
___



[arrays] [formatting] [strings] 
"""
def cms_selector(lst,st):
    if st == '':
        return lst
    return [x for x in lst if st in x.lower()]
print(cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], ""))