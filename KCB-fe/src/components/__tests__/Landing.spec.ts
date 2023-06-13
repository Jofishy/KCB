import { describe, it, expect, vi } from 'vitest'

import { mount } from '@vue/test-utils'
import Landing from '../Landing.vue'
import { afterEach } from 'vitest'

vi.mock("@/api/recipes", ()=>{
  const postRecipe = vi.fn();
  postRecipe.mockResolvedValue({message:"ok"});

  return {
    postRecipe
  }
});

describe('Landing', () => {
  afterEach(()=>{
    vi.restoreAllMocks();
  });
  
  it('renders properly', () => {
    const wrapper = mount(Landing, {});
    expect(wrapper.text()).toContain("Kiana's Cookbook")
    expect(wrapper.element.getElementsByTagName("input").length).toBe(1);
    expect(wrapper.element.getElementsByTagName("button").length).toBe(1);
  })
})
