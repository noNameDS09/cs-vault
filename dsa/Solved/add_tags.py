#!/usr/bin/env python3
"""
Script to add YAML frontmatter with tags to Obsidian markdown files in the Solved directory.
Tags are based on problem patterns and algorithms used.
"""

import os
import re

# Problem to tags mapping
problem_tags = {
    # Array / Two Pointers / Sliding Window
    "1_TwoSum.md": ["array", "hash-table", "two-pointers"],
    "11_ContainerWithMostWater.md": ["array", "two-pointers", "greedy"],
    "15_3Sum.md": ["array", "two-pointers", "sorting"],
    "167_TwoSumII_InputArrayIsSorted.md": ["array", "two-pointers", "binary-search"],
    "42_TrappingRainWater.md": ["array", "two-pointers", "stack", "prefix-sum"],
    "238_ProductOfArrayExceptSelf.md": ["array", "prefix-sum"],
    "287_FindTheDuplicateNumber.md": ["array", "two-pointers", "binary-search", "linked-list-cycle"],
    "128_LongestConsecutiveSequence.md": ["array", "hash-table", "union-find"],
    "217_ContainsDuplicates.md": ["array", "hash-table", "sorting"],
    "347_TopKFrequentElements.md": ["array", "hash-table", "heap", "quickselect"],
    "49_GroupAnagrams.md": ["array", "hash-table", "string", "sorting"],
    "239_SlidingWindowMaximum.md": ["array", "queue", "sliding-window", "monotonic-queue"],
    "739_DailyTemperatures.md": ["array", "stack", "monotonic-stack"],
    "84_LargestRectangleInHistogram.md": ["array", "stack", "monotonic-stack"],
    "853_CarFleet.md": ["array", "stack", "monotonic-stack", "sorting"],
    "2553_SeparateTheDigitsInAnArray.md": ["array", "math"],
    "1732_FindTheHighestAltitude.md": ["array", "prefix-sum"],
    "3866_FirstUniqueEvenElement.md": ["array", "hash-table"],
    "2996_SmallestMissingIntegerGreaterThanSequentialPrefixSum.md": ["array", "hash-table", "prefix-sum"],
    "3838_WeightedWordMapping.md": ["array", "hash-table", "string"],
    "3731_FindMissingElements.md": ["array", "hash-table"],
    "3982_SumOfIntegersWithMaximumDigitRange.md": ["array", "math"],
    "3612_ProcessStringWithSpecialOperationsI.md": ["array", "string", "simulation"],
    "3513_NumberOfUniqueXORTripletsI.md": ["array", "bit-manipulation", "hash-table"],
    "3514_NumberOfUniqueXORTripletsII.md": ["array", "bit-manipulation", "hash-table"],
    "3300_MinimumElementAfterReplacementWithDigitSum.md": ["array", "math", "simulation"],
    "3310_RemoveMethodsFromProject.md": ["array", "graph", "topological-sort"],
    "3090_MaximumLengthSubstringWithTwoOccurrences.md": ["array", "sliding-window", "hash-table", "string"],
    "2958_LengthOfLongestSubarrayWithAtMostKFrequency.md": ["array", "sliding-window", "hash-table"],
    "1967_NumberOfStringsThatAppearAsSubstringsInWord.md": ["array", "string", "trie", "hash-table"],
    "1260_Shift2DGrid.md": ["array", "matrix", "simulation"],
    "1291_SequentialDigits.md": ["array", "math", "enumeration"],
    "1331_RankTransformOfAnArray.md": ["array", "sorting", "hash-table"],
    "1464_MaximumProductOfTwoElementsInAnArray.md": ["array", "sorting", "heap"],
    "628_MaximumProductOfThreeNumbers.md": ["array", "sorting", "math"],
    "3536_MaximumProductOfTwoDigits.md": ["array", "math"],
    "3517_SmallestPalindromicRearrangementI.md": ["array", "string", "greedy", "hash-table"],
    "3499_MaximizeActiveSectionWithTradeI.md": ["array", "sliding-window", "prefix-sum"],
    "3471_FindTheLargestAlmostMissingInteger.md": ["array", "hash-table", "binary-search"],
    "3702_LongestSubsequenceWithNon-ZeroBitwiseXOR.md": ["array", "bit-manipulation", "dynamic-programming"],
    "4006_CountValidPrefixes.md": ["array", "string", "hash-table", "trie"],
    "2315_CountAsterisks.md": ["array", "string", "simulation"],
    "3014_MinimumNumberOfPushesToTypeWordI.md": ["array", "string", "greedy", "sorting"],
    "3016_MinimumNumberOfPushesToTypeWordII.md": ["array", "string", "greedy", "sorting", "heap"],
    "3867_SumOfGCDOfFormedPairs.md": ["array", "math", "number-theory"],
    
    # Linked List
    "2_AddTwoNumbers.md": ["linked-list", "math", "recursion"],
    "19_RemoveNthNodeFromEndOfList.md": ["linked-list", "two-pointers"],
    "20_ValidParentheses.md": ["stack", "string"],
    "21_MergeTwoSortedLists.md": ["linked-list", "recursion"],
    "23_MergeKSortedLists.md": ["linked-list", "divide-and-conquer", "heap", "merge-sort"],
    "25_ReverseNodesInK-Group.md": ["linked-list", "recursion"],
    "138CopyListWithRandomPointer.md": ["linked-list", "hash-table", "deep-copy"],
    "141_LinkedListCycle.md": ["linked-list", "two-pointers", "hash-table", "floyd-cycle-detection"],
    "143_ReorderList.md": ["linked-list", "two-pointers", "stack", "recursion"],
    "150_EvaluateReversePolishNotation.md": ["stack", "array", "math"],
    "155_MinStack.md": ["stack", "design"],
    "206_ReverseLinkedList.md": ["linked-list", "recursion", "two-pointers"],
    "2095_DeleteTheMiddleNodeOfALinkedList.md": ["linked-list", "two-pointers"],
    "2130_MaximumTwinSumOfALinkedList.md": ["linked-list", "two-pointers", "stack"],
    "74_SearchA2DMatrix.md": ["array", "binary-search", "matrix"],
    "1448_CountGoodNodesInBinaryTree.md": ["tree", "dfs", "bfs", "binary-tree"],
    
    # Binary Tree / BST
    "100_SameTree.md": ["tree", "dfs", "bfs", "binary-tree"],
    "102_BinaryTreeLevelOrderTraversal.md": ["tree", "bfs", "binary-tree"],
    "104_MaximumDepthOfBinaryTree.md": ["tree", "dfs", "bfs", "binary-tree"],
    "110_BalancedBinaryTree.md": ["tree", "dfs", "binary-tree"],
    "1448_CountGoodNodesInBinaryTree.md": ["tree", "dfs", "bfs", "binary-tree"],
    "199_BinaryTreeRightSideView.md": ["tree", "bfs", "dfs", "binary-tree"],
    "226_InvertBinaryTree.md": ["tree", "dfs", "bfs", "binary-tree"],
    "230_KthSmallestElementInABST.md": ["tree", "bst", "dfs", "inorder-traversal"],
    "235_LowestCommonAncestorOfABinarySearchTree.md": ["tree", "bst", "dfs"],
    "543_DiameterOfBinaryTree.md": ["tree", "dfs", "binary-tree"],
    "572_SubtreeOfAnotherTree.md": ["tree", "dfs", "binary-tree", "string-matching"],
    "98_ValidateBinarySearchTree.md": ["tree", "bst", "dfs", "binary-search"],
    "1448_CountGoodNodesInBinaryTree.md": ["tree", "dfs", "bfs", "binary-tree"],
    
    # Dynamic Programming
    "53_MaximumSubarray.md": ["array", "dynamic-programming", "divide-and-conquer", "kadane"],
    "198_HouseRobber.md": ["array", "dynamic-programming"],
    "416_PartitionEqualSubsetSum.md": ["array", "dynamic-programming", "bit-manipulation"],
    "746_MinCostClimbingStairs.md": ["array", "dynamic-programming"],
    "486_PredictTheWinner.md": ["array", "dynamic-programming", "game-theory", "minimax"],
    "1140_StoneGameII.md": ["array", "dynamic-programming", "game-theory", "suffix-sum"],
    "1406_StoneGameIII.md": ["array", "dynamic-programming", "game-theory"],
    "1510_StoneGameIV.md": ["dynamic-programming", "game-theory", "math"],
    "1563_StoneGameV.md": ["array", "dynamic-programming", "game-theory", "interval-dp"],
    "2029_StoneGameIX.md": ["array", "dynamic-programming", "game-theory", "math"],
    "877. Stone Game.md": ["array", "dynamic-programming", "game-theory", "math"],
    "307_RangeSumQueryMutable.md": ["array", "segment-tree", "binary-indexed-tree", "design"],
    "kmp_PatternSearch.md": ["string", "kmp", "dynamic-programming"],
    
    # Binary Search
    "7_ReverseInteger.md": ["math", "binary-search"],
    "33_SearchInRotatedSortedArray.md": ["array", "binary-search"],
    "34_FindFirstAndLastPositionOfElementInSortedArray.md": ["array", "binary-search"],
    "153_FindMinimumInRotatedSortedArray.md": ["array", "binary-search"],
    "704_BinarySearch.md": ["array", "binary-search"],
    "875_KokoEatingBananas.md": ["array", "binary-search"],
    "2770_MaximumNumberOfJumpsToReachTheLastIndex.md": ["array", "dynamic-programming", "binary-search", "segment-tree"],
    "3302_FindTheLexicographicallySmallestValidSequence.md": ["array", "binary-search", "greedy", "string"],
    
    # String
    "67_AddBinary.md": ["math", "string", "bit-manipulation", "simulation"],
    "796_RotateString.md": ["string", "string-matching"],
    "838_PushDominoes.md": ["string", "two-pointers", "simulation"],
    "125_ValidPalindrome.md": ["string", "two-pointers"],
    "1081_SmallestSubsequenceOfDistinctCharacters.md": ["string", "stack", "monotonic-stack", "greedy", "hash-table"],
    "763_PartitionLabels.md": ["string", "hash-table", "two-pointers", "greedy"],
    
    # Stack / Monotonic Stack
    "150_EvaluateReversePolishNotation.md": ["stack", "array", "math"],
    "155_MinStack.md": ["stack", "design"],
    "739_DailyTemperatures.md": ["array", "stack", "monotonic-stack"],
    "84_LargestRectangleInHistogram.md": ["array", "stack", "monotonic-stack"],
    "853_CarFleet.md": ["array", "stack", "monotonic-stack", "sorting"],
    "1081_SmallestSubsequenceOfDistinctCharacters.md": ["string", "stack", "monotonic-stack", "greedy", "hash-table"],
    
    # Heap / Priority Queue
    "23_MergeKSortedLists.md": ["linked-list", "divide-and-conquer", "heap", "merge-sort"],
    "239_SlidingWindowMaximum.md": ["array", "queue", "sliding-window", "monotonic-queue"],
    "347_TopKFrequentElements.md": ["array", "hash-table", "heap", "quickselect"],
    "3016_MinimumNumberOfPushesToTypeWordII.md": ["array", "string", "greedy", "sorting", "heap"],
    "1464_MaximumProductOfTwoElementsInAnArray.md": ["array", "sorting", "heap"],
    
    # Greedy
    "11_ContainerWithMostWater.md": ["array", "two-pointers", "greedy"],
    "42_TrappingRainWater.md": ["array", "two-pointers", "stack", "prefix-sum"],
    "763_PartitionLabels.md": ["string", "hash-table", "two-pointers", "greedy"],
    "875_KokoEatingBananas.md": ["array", "binary-search"],
    "3014_MinimumNumberOfPushesToTypeWordI.md": ["array", "string", "greedy", "sorting"],
    "3016_MinimumNumberOfPushesToTypeWordII.md": ["array", "string", "greedy", "sorting", "heap"],
    "3517_SmallestPalindromicRearrangementI.md": ["array", "string", "greedy", "hash-table"],
    
    # Graph / DFS / BFS
    "20_ValidParentheses.md": ["stack", "string"],
    "1331_RankTransformOfAnArray.md": ["array", "sorting", "hash-table"],
    "3310_RemoveMethodsFromProject.md": ["array", "graph", "topological-sort"],
    "102_BinaryTreeLevelOrderTraversal.md": ["tree", "bfs", "binary-tree"],
    "199_BinaryTreeRightSideView.md": ["tree", "bfs", "dfs", "binary-tree"],
    "1448_CountGoodNodesInBinaryTree.md": ["tree", "dfs", "bfs", "binary-tree"],
    
    # Trie
    "1967_NumberOfStringsThatAppearAsSubstringsInWord.md": ["array", "string", "trie", "hash-table"],
    "4006_CountValidPrefixes.md": ["array", "string", "hash-table", "trie"],
    "1081_SmallestSubsequenceOfDistinctCharacters.md": ["string", "stack", "monotonic-stack", "greedy", "hash-table"],
    
    # Bit Manipulation
    "3513_NumberOfUniqueXORTripletsI.md": ["array", "bit-manipulation", "hash-table"],
    "3514_NumberOfUniqueXORTripletsII.md": ["array", "bit-manipulation", "hash-table"],
    "3702_LongestSubsequenceWithNon-ZeroBitwiseXOR.md": ["array", "bit-manipulation", "dynamic-programming"],
    "3838_WeightedWordMapping.md": ["array", "hash-table", "string"],
    "3867_SumOfGCDOfFormedPairs.md": ["array", "math", "number-theory"],
    "67_AddBinary.md": ["math", "string", "bit-manipulation", "simulation"],
    
    # Math / Number Theory
    "7_ReverseInteger.md": ["math", "binary-search"],
    "66_PlusOne.md": ["array", "math"],
    "67_AddBinary.md": ["math", "string", "bit-manipulation", "simulation"],
    "1291_SequentialDigits.md": ["array", "math", "enumeration"],
    "2078_TwoFurthestHousesWithDifferentColors.md": ["array", "two-pointers"],
    "3867_SumOfGCDOfFormedPairs.md": ["array", "math", "number-theory"],
    "1510_StoneGameIV.md": ["dynamic-programming", "game-theory", "math"],
    "877. Stone Game.md": ["array", "dynamic-programming", "game-theory", "math"],
    
    # Design
    "155_MinStack.md": ["stack", "design"],
    "307_RangeSumQueryMutable.md": ["array", "segment-tree", "binary-indexed-tree", "design"],
    
    # Backtracking
    # (none explicitly, but some problems could use it)
    
    # Prefix Sum
    "238_ProductOfArrayExceptSelf.md": ["array", "prefix-sum"],
    "42_TrappingRainWater.md": ["array", "two-pointers", "stack", "prefix-sum"],
    "1732_FindTheHighestAltitude.md": ["array", "prefix-sum"],
    "2996_SmallestMissingIntegerGreaterThanSequentialPrefixSum.md": ["array", "hash-table", "prefix-sum"],
    "3499_MaximizeActiveSectionWithTradeI.md": ["array", "sliding-window", "prefix-sum"],
    "1140_StoneGameII.md": ["array", "dynamic-programming", "game-theory", "suffix-sum"],
    
    # Interval DP
    "1563_StoneGameV.md": ["array", "dynamic-programming", "game-theory", "interval-dp"],
    
    # Union Find
    "128_LongestConsecutiveSequence.md": ["array", "hash-table", "union-find"],
}

def add_frontmatter(filepath, tags):
    """Add YAML frontmatter with tags to a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if frontmatter already exists
    if content.startswith('---'):
        # Already has frontmatter, check if tags exist
        if 'tags:' in content.split('---')[1]:
            print(f"  Already has tags: {os.path.basename(filepath)}")
            return False
    
    # Create tags string in YAML format
    tags_str = 'tags:\n' + '\n'.join([f'  - {tag}' for tag in tags])
    
    # Create frontmatter
    frontmatter = f'---\n{tags_str}\n---\n\n'
    
    # Add frontmatter at the beginning
    new_content = frontmatter + content
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  Added tags to: {os.path.basename(filepath)}")
    return True

def main():
    solved_dir = r"D:\Programming\DSA\dsa\Solved"
    
    # Get all .md files
    md_files = [f for f in os.listdir(solved_dir) if f.endswith('.md')]
    
    updated = 0
    skipped = 0
    
    for filename in md_files:
        filepath = os.path.join(solved_dir, filename)
        
        if filename in problem_tags:
            tags = problem_tags[filename]
            if add_frontmatter(filepath, tags):
                updated += 1
            else:
                skipped += 1
        else:
            print(f"  No tags mapping for: {filename}")
            skipped += 1
    
    print(f"\nDone! Updated: {updated}, Skipped/No mapping: {skipped}")

if __name__ == "__main__":
    main()