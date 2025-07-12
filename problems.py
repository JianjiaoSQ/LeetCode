import os
import sys
from datetime import datetime

def main():
    # 配置参数
    if len(sys.argv) < 2:
        print("Usage: python problems.py <problems_directory> [output_file]")
        print("Example: python problems.py ./problems all_solutions.md")
        sys.exit(1)
    
    problems_dir = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "solutions.md"
    
    # 初始化统计信息
    total = 0
    success = 0
    skipped = 0
    
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
            
            # 添加到输出
            content.append(f"## {problem_dir}\n\n")
            content.append(f"{md_content}\n\n")
            content.append("### 题解\n\n```python\n")
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
        f.writelines(content)
    
    print(f"\n处理完成! 结果已保存到 {output_file}")
    print(f"统计: 总数={total}, 成功={success}, 跳过={skipped}")

if __name__ == "__main__":
    main()