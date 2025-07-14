import os
import sys
from datetime import datetime

def main():
    # # 配置参数
    # if len(sys.argv) < 2:
    #     print("Usage: python problems.py <problems_directory> [output_file]")
    #     print("Example: python problems.py ./problems all_solutions.md")
    #     sys.exit(1)
    
    problems_dir = './'
    output_file = "题解.md"
    
    # 初始化统计信息
    total = 0
    success = 0
    skipped = 0

    mulu = ['# 目录\n']
    mapping = {
      "0001-TwoSum-Easy": "两数之和-简单",
      "0002-AddTwoNumbers-Medium": "两数相加-中等",
      "0003-LongestSubstringWithoutRepeatingCharacters-Medium": "无重复字符的最长子串-中等",
      "0005-LongestPalindromicSubstring-Medium": "最长回文子串-中等",
      "0011-ContainerWithMostWater-Medium": "盛最多水的容器-中等",
      "0017-LetterCombinationsofaPhoneNumber-Medium": "电话号码的字母组合-中等",
      "0019-RemoveNthNodeFromEndofList-Medium": "删除链表的倒数第N个节点-中等",
      "0020-ValidParentheses-Easy": "有效的括号-简单",
      "0021-MergeTwoSortedLists-Easy": "合并两个有序链表-简单",
      "0022-GenerateParentheses-Medium": "括号生成-中等",
      "0056-MergeIntervals-Medium": "合并区间-中等",
      "0070-ClimbingStairs-Easy": "爬楼梯-简单",
      "0074-Searcha2DMatrix-Medium": "搜索二维矩阵-中等",
      "0094-BinaryTreeInorderTraversal-Easy": "二叉树的中序遍历-简单",
      "0101-SymmetricTree-Easy": "对称二叉树-简单",
      "0104-MaximumDepthofBinaryTree-Easy": "二叉树的最大深度-简单",
      "0121-BestTimetoBuyandSellStock-Easy": "买卖股票的最佳时机-简单",
      "0125-ValidPalindrome-Easy": "验证回文串-简单",
      "0141-LinkedListCycle-Easy": "环形链表-简单",
      "0160-IntersectionofTwoLinkedLists-Easy": "相交链表-简单",
      "0198-HouseRobber-Medium": "打家劫舍-中等",
      "0206-ReverseLinkedList-Easy": "反转链表-简单",
      "0215-KthLargestElementinanArray-Medium": "数组中的第K个最大元素-中等",
      "0234-PalindromeLinkedList-Easy": "回文链表-简单",
      "0300-LongestIncreasingSubsequence-Medium": "最长递增子序列-中等",
      "0617-MergeTwoBinaryTrees-Easy": "合并二叉树-简单"
    }
    # 准备输出内容
    content = []
    content.append(f"# 题解合集\n\n")
    content.append(f"*生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")

    # 遍历问题目录
    for problem_dir in sorted(os.listdir(problems_dir)):
        dir_path = os.path.join(problems_dir, problem_dir)
        if not os.path.isdir(dir_path):
            continue
            
        total += 1
        print(f"正在处理: {problem_dir}")
        
        # 查找文件（支持多种常见命名方式）
        md_files = []
        py_files = []
        
        for f in os.listdir(dir_path):
            lower_f = f.lower()
            if lower_f.endswith('.md'):
                md_files.append(os.path.join(dir_path, f))
            elif lower_f.endswith('.py'):
                py_files.append(os.path.join(dir_path, f))
        
        # 检查文件是否存在
        if not md_files or not py_files:
            print(f"  警告: 目录 {problem_dir} 中缺少.md或.py文件")
            skipped += 1
            continue
        
        # 取第一个找到的md和py文件
        md_file = md_files[0]
        py_file = py_files[0]

        # 读取内容
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                md_content = f.read()
            with open(py_file, 'r', encoding='utf-8') as f:
                py_content = f.read()

            # 添加目录
            cn_title = mapping.get(problem_dir) if mapping.get(problem_dir) else problem_dir
            flag = cn_title + '-题解'
            mulu.append(f"- [{cn_title}](#{flag})\n")
            # 添加到输出
            content.append(f"## {cn_title}\n")
            content.append(f"{md_content}\n\n")
            content.append(f'''<a id="{flag}"></a>\n''')
            content.append(f"### {flag}\n```python\n\n")
            content.append(f"{py_content}\n```\n\n")
            success += 1
        except Exception as e:
            print(f"  处理 {problem_dir} 时出错: {str(e)}")
            skipped += 1
    
    # 添加统计信息
    content.append("## 统计\n\n")
    content.append(f"- 总题目数: {total}\n")
    content.append(f"- 成功处理: {success}\n")
    content.append(f"- 跳过题目: {skipped}\n")
    
    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(mulu + content)
    
    print(f"\n处理完成! 结果已保存到 {output_file}")
    print(f"统计: 总数={total}, 成功={success}, 跳过={skipped}")

if __name__ == "__main__":
    main()